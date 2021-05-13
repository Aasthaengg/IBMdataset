N, K = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
X = sorted([p[0] for p in P])
Y = sorted([p[1] for p in P])

ans = 10**20
for i in range(N-1):
    for j in range(i+1, N):
        x0 = X[i]
        x1 = X[j]

        for k in range(N-1):
            for l in range(k+1, N):
                y0 = Y[k]
                y1 = Y[l]

                c = 0
                for m in range(N):
                    if x0 <= P[m][0] <= x1 and y0 <= P[m][1] <= y1:
                        c += 1

                if c >= K:
                    ans = min(ans, (x1-x0)*(y1-y0))

print(ans)
