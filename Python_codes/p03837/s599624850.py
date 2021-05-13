n,m = map(int, input().split())
l = []
for i in range(m):
    l.append(list(map(int,input().split())))

wf=[[10**10 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b,c = l[i]
    wf[a-1][b-1] = c
    wf[b-1][a-1] = c
for i in range(n):
    wf[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            wf[i][j] = min(wf[i][j],wf[i][k]+wf[k][j])

ans=0
for edge in l:
    ok=False
    for i in range(n):
        for j in range(n):
            dist = wf[i][j]
            if dist == wf[i][edge[0]-1] + edge[2] + wf[edge[1]-1][j]:
                ok=True
    if not ok:
        ans+=1
print(ans)