n,m = map(int, input().split())
ans=1
div=10**9+7

def func(ans,x):
  for i in range(1,x+1):
    ans*=i
    ans%=div
  return ans

if abs(n-m)>1:
  ans = 0
else:
  ans = func(ans,n)
  ans = func(ans,m)
  if abs(n-m)==0:
    ans*=2
    ans%=div

print(ans)