N, *XY = map(int, open(0).read().split())
X = XY[::2]
Y = XY[1::2]
ans = N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        p = X[i] - X[j]
        q = Y[i] - Y[j]
        cnt = 0
        for k in range(N):
            for l in range(N):
                if k == l:
                    continue
                if X[k] - X[l] == p and Y[k] - Y[l] == q:
                    cnt += 1
        ans = min(ans, N - cnt)
print(ans)
