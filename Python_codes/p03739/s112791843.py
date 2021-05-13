n = int(input())
a = list(map(int,input().split()))

def calc(t):
  ans = su = 0
  for i in range(n):
    su += a[i]
    if i % 2 == t:
      if su > 0:
        pass
      else:
        x = 1 - su
        ans += abs(x)
        su = 1
    else:
      if su < 0:
        pass
      else:
        x = - 1 - su
        ans += abs(x)
        su = -1
  return ans
print(min(calc(1), calc(0)))