import sys,math,collections,itertools
input = sys.stdin.readline

N,M,R=list(map(int,input().split()))
r=list(map(int,input().split()))
ABC = [[float('inf')]*(N+1) for _ in range(N+1)]
#条件のうち、重複経路は最短のみ残す
for _ in range(M):
    a,b,c = map(int,input().split())
    if ABC[a][b]>c:
        ABC[a][b]=c
        ABC[b][a]=c

#各頂点間の最小距離 Warshall-Floyd
dist = [[float('inf')]*(N+1) for _ in range(N+1)]
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            ABC[i][j] = min(ABC[i][j],ABC[i][k] + ABC[k][j])

rotate = itertools.permutations(r)
ans = float('inf')
for rot in rotate:
    tmp = 0
    flag = 0
    for i in range(len(rot)-1):
        tmp +=ABC[rot[i]][rot[i+1]]
        if tmp>ans:
            flag = 1
            break
    if flag==0:
        ans = min(ans,tmp)
print(ans)
