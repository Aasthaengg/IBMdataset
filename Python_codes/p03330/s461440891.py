import itertools
N,C = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(N)]

delta = [[0]*C for _ in range(3)]

for i in range(N):
    for j in range(N):
        for to in range(C):
            delta[(i+j)%3][to] += D[c[i][j]-1][to]
ans = 1e100
for x,y,z in itertools.permutations(range(C),3):
    ans = min(ans, delta[0][x] + delta[1][y] + delta[2][z])
print(ans)
