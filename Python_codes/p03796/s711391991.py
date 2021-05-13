#a,b=map(int,input().split())
n=int(input())
mod=10**9+7
#s=input()
ans=1
for i in range(1,n+1):
  ans*=(i%mod)
  ans%=mod
print(ans%mod)