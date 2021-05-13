n,m = map(int, input().split())
link = [[] for _ in range(n)]
inc=[0]*n
for _ in range(m):
    x,y = list(map(int,input().split()))
    link[x-1].append(y-1)
    inc[y-1]+=1

s=[]
for i in range(len(inc)):
    if inc[i]==0:
        s.append(i)
res=[]
while s:
    nxt=s.pop()
    res.append(nxt)
    for m in link[nxt]:
        inc[m]-=1
        if inc[m]==0:
            s.append(m)

path=[-1]*n
for now in res:
    if path[now]==-1:
        path[now]=0
    for nxt in link[now]:
        path[nxt] = max(path[nxt],path[now]+1)

print(max(path))