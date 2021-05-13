n,k=map(int,input().split())
use=[(i,j) for i in range(2,n) for j in range(i+1,n+1)]
if k>(n-2)*(n-1)//2:
  print(-1)
  exit()
ans=[]
for i in range(2,n+1):
  ans+=[(1,i)]
for _ in range((n-2)*(n-1)//2-k):
  ans+=[use.pop()]
print(len(ans))
for i in ans:
  print(*i)