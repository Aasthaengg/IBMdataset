n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod=10**9+7
ctx=0;cty=0
for i in range(n):
  ctx+=(2*i-n+1)*x[i]
  ctx%=mod
for i in range(m):
  cty+=(2*i-m+1)*y[i]
  cty%=mod
print((ctx*cty)%mod)