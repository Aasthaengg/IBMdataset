N,T=map(int,input().split())
L=list(map(int,input().split()))
L=L+[10**9+T]
ans=0
for i in range(N):
  ans+=min(T,L[i+1]-L[i])
print(ans)