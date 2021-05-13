N,K=map(int,input().split())
L=sorted([int(input()) for i in range(N)])
ans=10**9+1
for i in range(K-1,N):
  ans=min(ans,L[i]-L[i-(K-1)])
print(ans)