N, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

w0 = X[0][0]
ctr = [[] for _ in range(4)]
for w, v in X:
    ctr[w - w0].append(v)

for n in range(4):
    values = sorted(ctr[n], reverse=True)
    s = [0] * (len(values) + 1)
    for i in range(len(values)):
        s[i + 1] = s[i] + values[i]
    ctr[n] = s

ans = 0
for i in range(len(ctr[0])):
    for j in range(len(ctr[1])):
        for k in range(len(ctr[2])):
            for l in range(len(ctr[3])):
                tmp = ctr[0][i] + ctr[1][j] + ctr[2][k] + ctr[3][l]
                w = w0 * i + (w0 + 1) * j + (w0 + 2) * k + (w0 + 3) * l
                if w <= W:
                    ans = max(ans, tmp)

print(ans)
