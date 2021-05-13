N,M=map(int, input().split())
E=[]
for i in range(M):
    a,b,c=map(int, input().split())
    E.append((a-1,b-1,c))
INF=1<<60

D=[[INF]*N for _ in range(N)]
for a,b,c in E:
    D[a][b]=D[b][a]=c
for z in range(N):
    for x in range(N):
        Dx=D[x]
        for y in range(N):
            Dx[y]=min(Dx[y], Dx[z]+D[z][y])

ans=M
for a,b,c in E:
    if D[a][b]==c: ans-=1
print(ans)
