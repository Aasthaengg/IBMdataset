n,k=map(int,input().split())

if n>=k:
  ans=abs(n-((n+k//2)//k)*k)

else:
  ans=min(n,abs(n-k))

print(ans)