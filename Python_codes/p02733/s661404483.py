from itertools import product, combinations_with_replacement
H, W, K = map(int, input().split())
S = tuple(tuple(map(int, list(input()))) for _ in range(H))

choko = [[0]*W for _ in range(H)]

ans = 10**18

for divide in product(range(2), repeat=H - 1):
    cut = sum(divide)
    row = [0]
    for d in divide:
        if d:
            row.append(row[-1] + 1)
        else:
            row.append(row[-1])

    r = row[-1] + 1
    for i in range(r):
        for j in range(W):
            choko[i][j] = 0
    for i in range(H):
        for j in range(W):
            choko[row[i]][j] += S[i][j]

    if any(choko[i][0] > K for i in range(r)):
        continue

    now = [0] * r
    for j in range(W):
        if any(now[i] + choko[i][j] > K for i in range(r)):
            cut += 1
            now = [choko[i][j] for i in range(r)]
        else:
            for i in range(r):
                now[i] += choko[i][j]

    ans = min(ans, cut)

print(ans)