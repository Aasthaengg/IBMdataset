N, C = map(int, input().split())
D = []
for _ in range(C):
    D.append([int(d) for d in input().split()])
t = [[0 for _ in range(C)] for _ in range(3)]
for i in range(N):
    for j, c in enumerate(input().split()):
        c = int(c) - 1
        t[(i + j) % 3][c] += 1

ans = float('inf')
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            res = 0
            for l in range(C):
                res += D[l][i] * t[0][l]
                res += D[l][j] * t[1][l]
                res += D[l][k] * t[2][l]
            ans = min(ans, res)
print(ans)