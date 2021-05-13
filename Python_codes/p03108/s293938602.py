n,m=map(int,input().split())

par=[i for i in range(n)]
size=[1]*n

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

ans=[n*(n-1)//2]
bridge=[]

for i in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  bridge.append([a,b])

bridge.reverse()
bridge.pop()

for i in bridge:
  if find(i[0]) != find(i[1]):
    ans.append(ans[-1]-size[find(i[0])]*size[find(i[1])])
    union(i[0],i[1])
  else:
    ans.append(ans[-1])


ans.reverse()

for i in ans:
  print(i)