N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

x = sorted(v for v, _ in X)
y = sorted(v for _, v in X)
ans = 10 ** 20
for i in range(N - 1):
    for j in range(i + 1, N):
        for k in range(N - 1):
            for l in range(k + 1, N):
                x1 = x[i]
                x2 = x[j]
                y1 = y[k]
                y2 = y[l]
                num = 0
                for n in range(N):
                    if x1 <= X[n][0] <= x2 and y1 <= X[n][1] <= y2:
                        num += 1
                if num >= K:
                    ans = min(ans, (x2 - x1) * (y2 - y1))

print(ans)
