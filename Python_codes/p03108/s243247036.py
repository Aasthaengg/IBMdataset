N,M=map(int,input().split())
bridge=[]
for i in range(M):
  a,b=map(int,input().split())
  bridge.append((a-1,b-1))
bridge.reverse()
par=[i for i in range(N)]
size=[1 for i in range(N)]
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:
    if size[x]<size[y]:
      par[x]=par[y]
      size[y]+=size[x]
    else: 
      par[y]=par[x]
      size[x]+=size[y]
  else:
    return
now=int(N*(N-1)/2)
ans=[]
ans.append(now)
for i in range(M-1):
  a=bridge[i][0]
  b=bridge[i][1]
  if find(a)==find(b):
    ans.append(now)
  else:
    now-=size[find(a)]*size[find(b)]
    ans.append(now)
  union(a,b)
ans.reverse()
print(*ans)