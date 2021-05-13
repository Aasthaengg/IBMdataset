N,C = map(int, input().split())
# D[i][j]: 色iから色jに塗り替える場合のコスト
D = [[int(i) for i in input().split()] for _ in range(C)]

cnt = [[0] * C for _ in range(3)]
for i in range(1, N + 1):
    line = [int(i) for i in input().split()]
    for j, c in enumerate(line, start=1):
        cnt[(i + j) % 3][c - 1] += 1

ans = float("inf")
for i in range(C):
    for j in range(C):
        if i == j: continue
        for k in range(C):
            if i == k or j == k: continue
            cost = 0
            for x in range(C):
                cost += D[x][i] * cnt[0][x]
                cost += D[x][j] * cnt[1][x]
                cost += D[x][k] * cnt[2][x]
            
            ans = min(ans, cost)

print(ans)