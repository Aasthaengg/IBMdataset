N,K=map(int,input().split())
for i in range(N):
  if i==0:
    ans=K
  if i>0:
    ans*=(K-1)
print(ans)