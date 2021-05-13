import itertools

N,M,R = map(int,(input().split()))
r = list(map(lambda x:int(x)-1,(input().split())))

dist = [[float("inf")]*N for _ in range(N)]

for i in range(M):
    a,b,c = map(int,(input().split()))
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
for i in range(N):
    dist[i][i] = 0

def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d

dist = warshall_floyd(dist)

min_ans = float("inf")
for perm in itertools.permutations(r):
    ans = 0
    for i in range(len(r)-1):
        ans += dist[perm[i]][perm[i+1]]
    min_ans = min(ans,min_ans)

print(min_ans)