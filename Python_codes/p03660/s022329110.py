import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def main():
  n = int(input())
  F = [[] for _ in range(n)]
  for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    F[a].append(b)
    F[b].append(a)
  seenB = [False]*n
  seenW = [False]*n
  distB = [0]*n
  distW = [0]*n
  def dfs(v, seen, dist):
    seen[v] = True
    for nv in F[v]:
      if seen[nv]:
        continue
      dist[nv] = dist[v] + 1
      dfs(nv, seen, dist)
  dfs(0, seenB, distB)
  dfs(n-1, seenW, distW)
  b, w = 0, 0
  for i in range(n):
    if distB[i] <= distW[i]:
      b += 1
    else:
      w += 1
  if b > w:
    print("Fennec")
  else:
    print("Snuke")
      
if __name__ == '__main__':
  main()