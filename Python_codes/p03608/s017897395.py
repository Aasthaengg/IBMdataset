from itertools import permutations
N,M,R = list(map(int,input().split()))
r = list(map(int,input().split()))
r = [i-1 for i in r]
ABC = [[float('inf') for i in range(N)]for j in range(N)]
for i in range(N):
    ABC[i][i] = 0
for i in range(M):
    a,b,c = list(map(int,input().split()))
    a -= 1
    b -= 1
    ABC[a][b] = c
    ABC[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            ABC[i][j] = min(ABC[i][j],ABC[i][k]+ABC[k][j])
ans = float('inf')
for i in permutations(r):
    cost = 0
    now = i[0]
    for j in range(1,len(i)):
        cost += ABC[now][i[j]]
        now = i[j]
    ans = min(ans,cost)
print(ans)