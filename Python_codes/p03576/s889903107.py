N, K = map(int, input().split())

X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = float('INF')

for left in range(N):
    for right in range(N):
        for top in range(N):
            for bottom in range(N):
                if X[right]-X[left] <= 0:
                    continue
                if Y[top]-Y[bottom] <= 0:
                    continue
                cnt = 0
                for i in range(N):
                    if X[left] <= X[i] <= X[right] and Y[bottom] <= Y[i] <= Y[top]:
                        cnt += 1
                if cnt >= K:
                    ans = min(ans, (X[right]-X[left])*(Y[top]-Y[bottom]))

print(ans)
