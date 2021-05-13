N,K=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(K):
  ans+=l[-i-1]
print(ans)