
from collections import defaultdict

N,C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]
grid = [tuple(map(int, input().split())) for _ in range(N)]


# mod_x : (i+j)%3がxで、keyは色、valueは個数
mod_0 = defaultdict(int)
mod_1 = defaultdict(int)
mod_2 = defaultdict(int)


for i in range(N):
    for j in range(N):
        if (i+1 + j+1) % 3 == 0:
            mod_0[grid[i][j]] += 1
        elif (i+1 + j+1) % 3 == 1:
            mod_1[grid[i][j]] += 1
        elif (i+1 + j+1) % 3 == 2:
            mod_2[grid[i][j]] += 1

ans = float("inf")
# mod_0のマスにあるものをiに、mod_1のものをjに、mod_2のものをkに塗り替える
for i in range(C):
    for j in range(C):
        if i == j: continue
        for k in range(C):
            if k in [i,j]:
                continue

            total = 0
            for prev,cnt in mod_0.items():
                total += D[prev-1][i] * cnt
            for prev,cnt in mod_1.items():
                total += D[prev-1][j] * cnt
            for prev,cnt in mod_2.items():
                total += D[prev-1][k] * cnt

            ans = min(ans, total)

print(ans)
