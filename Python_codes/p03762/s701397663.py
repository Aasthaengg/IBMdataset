n,m=map(int,input().split())
x=[0]+list(map(int,input().split()))
y=[0]+list(map(int,input().split()))
mod=10**9+7
a1,a2=0,0
for k in range(1,n+1):
  a1+=(k*2-n-1)*x[k]
for k in range(1,m+1):
  a2+=(k*2-m-1)*y[k]
print((a1*a2)%mod)