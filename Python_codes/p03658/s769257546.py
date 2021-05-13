N,K=map(int,input().split())
l=list(map(int,input().split()))
check=sorted(l,reverse=True)
ans=0
for i in range(0,K):
  ans+=check[i]
print(ans)
