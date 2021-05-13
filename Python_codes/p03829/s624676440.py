# D - Walk and Teleport
n,a,b=map(int,input().split())
x=list(map(int,input().split()))
dist=[]

for i in range(n-1):
    dist.append(x[i+1]-x[i])
ans=0
for i in range(len(dist)):
    if dist[i]*a<b:
        ans+=dist[i]*a
    else:
        ans+=b
print(ans)