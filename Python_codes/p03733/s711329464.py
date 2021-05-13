n,t=map(int,input().split())
ti=list(map(int,input().split()))
ans=t
p=0
dist=[]
for i in range(n-1):
  dist.append(ti[i+1]-ti[i])
for i in dist:
  ans+=min(i,t)
print(ans)