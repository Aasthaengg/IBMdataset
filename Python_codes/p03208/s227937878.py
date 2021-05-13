n,k=map(int,input().split())
H=[int(input()) for i in range(n)]
H.sort()
ans=10**9
for i in range(n-k+1):
  ans = min(ans,H[i+k-1]-H[i])
print(ans)