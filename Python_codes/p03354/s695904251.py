n,m=map(int,input().split())
p=list(map(int,input().split()))
xy=[list(map(int,input().split())) for _ in range(m)]
l=[i for i in range(n)]
def root(x):
  if x==l[x]:
    return x
  l[x]=root(l[x])
  return l[x]
for x,y in xy:
  a=root(x-1)
  b=root(y-1)
  if a!=b:
    l[b]=a
cnt=0
for i in range(n):
  if root(p[i]-1)==root(i):
    cnt+=1
print(cnt)
