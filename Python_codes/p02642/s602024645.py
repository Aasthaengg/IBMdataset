import sys
sys.setrecursionlimit(2147483647)
input=sys.stdin.readline

def main():
  n = int(input())
  a = list(map(int, input().split(' ')))
  a.sort()
  a_max = a[-1]
  b = 0
  db = [0] * a_max
  for i in range(1, n-1):
    if a[i] != a[i+1] and a[i] != a[i-1]:
      db[a[i]-1] = 1
  if n == 1 or a[0] != a[1]:
    db[a[0]-1] = 1
  if n > 1 and a[-1] != a[-2]:
    db[-1] = 1
  for i in a:
    t = 2
    while(i * t <= a_max):
      db[i*t-1] = 0
      t += 1
  print(sum(db))
  

if __name__=='__main__':
  main()