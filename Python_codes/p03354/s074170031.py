n,m=map(int,input().split())
p=list(map(lambda x:int(x)-1,input().split()))
xy=[list(map(int,input().split())) for _ in range(m)]
g=[[]for _ in range(n)]
for x,y in xy:
  g[x-1].append(y-1)
  g[y-1].append(x-1)
# 連結成分を探索
renktsu=[]
seen=[-1]*n
todo={i for i in range(n)}
while todo:
  t0=todo.pop()
  todo1=[t0]
  while todo1:
    t=todo1.pop()
    seen[t]=t0
    todo.discard(t)
    l=g[t]
    for li in l:
      if seen[li]==-1:
        todo1.append(li)
ans=0
for i in range(n):
  if seen[i]==seen[p[i]]:
    ans+=1
print(ans)
