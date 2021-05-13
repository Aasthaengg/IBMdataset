import sys

def main():
  out = 0
  for i in range(1, n+1):
    if dp[i]:
        di = dp[i]
        if di > out:
            out = di
    else:
        di = cal(i)
        if di > out:
            out = di
  print(out)

def cal(a):
  if xy[a]:
    ans = 0
    for b in xy[a]:
      if dp[b]:
        num = dp[b]
      else:
        num = cal(b)
        dp[b] = num
      if num+1 > ans:
        ans = num+1
    return ans
  return 0

if __name__ == "__main__":
  sys.setrecursionlimit(100000)
  n, m = map(int, input().split())
  xy = [set() for _ in range(n+1)]
  dp = [None]*(n+1)
  for _ in range(m):
    x, y = map(int, input().split())
    xy[x].add(y)
  main()

