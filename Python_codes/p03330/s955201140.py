import sys
input = sys.stdin.readline

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(lambda x: int(x)-1, input().split())) for N in range(N)]
val = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        for k in range(C):
            val[(i + j) % 3][k] += D[c[i][j]][k]
ans = float('inf')
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            ans = min(ans, val[0][i] + val[1][j] + val[2][k])
print(ans)