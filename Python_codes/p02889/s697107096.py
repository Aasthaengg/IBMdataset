import sys

def main():
  input = sys.stdin.readline
  n, m, l = map(int, input().split())
  
  inf = pow(10, 10)
  towns = [[inf]*n for _ in range(n)]
  
  for _ in range(m):
    a, b, c = map(int, input().split())
    if c > l:
      continue
    towns[a-1][b-1] = c
    towns[b-1][a-1] = c
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if towns[i][j] > towns[i][k]+towns[k][j] and l >= towns[i][k]+towns[k][j]:
          towns[i][j] = towns[i][k]+towns[k][j]
  
  for i in range(n):
    for j in range(n):
      if towns[i][j] == inf:
        continue
      towns[i][j] = 0
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if towns[i][j] > towns[i][k]+towns[k][j]+1:
          towns[i][j] = towns[i][k]+towns[k][j]+1

  q = int(input())
  for _ in range(q):
    s, t = map(int, input().split())
    print(towns[s-1][t-1] if towns[s-1][t-1] != inf else -1)

if __name__ == "__main__":
  main()