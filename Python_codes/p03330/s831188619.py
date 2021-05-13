from itertools import permutations

N, C = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

cnt = [[0] * C for _ in range(3)]

for i in range(N):
    for j in range(N):
        cnt[(i + j) % 3][grid[i][j] - 1] += 1

ans = N * N * 1000 + 10
for color in permutations(range(C), 3):
    dis = 0
    for i in range(3):
        for j in range(C):
            d = D[j][color[i]]
            num = cnt[i][j]
            dis += d * num

    ans = min(ans, dis)

print(ans)
