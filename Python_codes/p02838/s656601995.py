n=int(input())
a=list(map(int,input().split()))

mod=10**9+7

ans=0
for i in range(60):
  on=0
  for j in a:
    if (j>>i)&1:
      on+=1
  ans+=(on*(n-on))*(2**i)
  ans%=mod

print(ans)