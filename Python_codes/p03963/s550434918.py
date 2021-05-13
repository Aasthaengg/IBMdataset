N,K=map(int,input().split())

ans=1
for i in range(N):
  if i==0:
    ans *= K
    continue
  ans *= K-1
  
print(ans)