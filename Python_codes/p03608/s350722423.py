import copy

N,M,R=map(int,input().split())
r=list(map(int,input().split()))
d=[[10**15 for i in range(0,N+1)] for i in range(0,N+1)]
for i in range(0,M):
    a,b,c=map(int,input().split())
    d[a][b]=c
    d[b][a]=c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if d[i][j]>d[i][k]+d[k][j]:
                d[i][j]=d[i][k]+d[k][j]

ans=10**15
def dfs(load,cost,last):
    global ans
    if len(load)==R:
        if ans>cost:
            ans=cost

    elif len(load)!=0:
        for city in r:
            if not city in load:
                a=copy.copy(load)
                a.add(city)
                dfs(a,cost+d[last][city],city)

    else:
        for city in r:
            dfs(set([city]),0,city)



dfs(set([]),0,0)

print(ans)