n=int(input())
mod=10**9+7
pow=1
for i in range(1,n+1):
  pow*=i
  pow%=mod
print(pow)