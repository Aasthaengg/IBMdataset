from collections import Counter

N, C = [int(_) for _ in input().split()]

D = [[int(_) for _ in input().split()] for _ in range(C)]

cnt = [Counter() for _ in range(3)]
for i in range(N):
    tmp = [int(_) for _ in input().split()]
    for j in range(N):
        idx = (i + 1 + j + 1) % 3
        cnt[idx][tmp[j] - 1] += 1

vals = [[0] * C for _ in range(3)]
for i in range(3):
    for j in range(C):
        a = cnt[i][j]
        if a <= 0: continue
        for k in range(C):  # k 色に揃えるコスト
            vals[i][k] += D[j][k] * a
    # print(vals[i])

ans = 1e12
for x in range(C):
    for y in range(C):
        if x == y: continue
        for z in range(C):
            if x == z or y == z: continue
            ans = min(ans, vals[0][x] + vals[1][y] + vals[2][z])
print(ans)
