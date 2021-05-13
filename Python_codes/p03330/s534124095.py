from collections import Counter

N, C = [int(_) for _ in input().split()]

D = [[int(_) for _ in input().split()] for _ in range(C)]

cnt = [Counter() for _ in range(3)]
for i in range(N):
    tmp = [int(_) for _ in input().split()]
    for j in range(N):
        idx = (i + 1 + j + 1) % 3
        cnt[idx][tmp[j] - 1] += 1

ans = 1e12
for x in range(C):
    for y in range(C):
        if x == y: continue
        for z in range(C):
            if x == z or y == z: continue
            tmp = 0
            for i in range(C):
                tmp += cnt[0][i] * D[i][x]
                tmp += cnt[1][i] * D[i][y]
                tmp += cnt[2][i] * D[i][z]
            ans = min(ans, tmp)
print(ans)
