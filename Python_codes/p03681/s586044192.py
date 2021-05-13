from math import factorial as f
n,m=map(int,input().split())
if abs(n-m) >= 2:
  print(0)
  quit()
if n == m:
  print(f(n)*f(m)*2%(10**9+7))
else:
  print(f(max(m,n))*f(min(m,n))%(10**9+7))