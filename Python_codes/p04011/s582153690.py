import sys
n,k,x,y = map(int,sys.stdin.read().split())
high=n-k
ans=0
if high > 0:
  ans=x*k+high*y
else:
  ans=n*x
print(ans)
