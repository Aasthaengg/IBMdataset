N, W = [int(_) for _ in input().split()]

items = [[] for _ in range(4)]
w1, v = [int(_) for _ in input().split()]
items[0].append(v)

for i in range(N - 1):
    w, v = [int(_) for _ in input().split()]
    items[w - w1].append(v)

for i in range(4):
    items[i].sort(reverse=True)

S = []
for i in range(4):
    l = len(items[i])
    s = [0] * (l + 1)
    for j in range(l):
        s[j + 1] = items[i][j] + s[j]
    S.append(s)

ans = 0
for i in range(len(items[0]) + 1):
    for j in range(len(items[1]) + 1):
        for k in range(len(items[2]) + 1):
            for l in range(len(items[3]) + 1):
                v = S[0][i] + S[1][j] + S[2][k] + S[3][l]
                w = w1 * i + (w1 + 1) * j + (w1 + 2) * k + (w1 + 3) * l
                if w <= W:
                    ans = max(v, ans)
print(ans)
