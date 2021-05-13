n, k = map(int, input().split())
xy = []
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    xy.append([x, y])
X.sort()
Y.sort()
ans = float("inf")
for i in range(n):
    for j in range(i + 1, n):
        for l in range(n):
            for m in range(l + 1, n):
                count = 0
                for o in range(n):
                    if X[i] <= xy[o][0] <= X[j] and Y[l] <= xy[o][1] <= Y[m]:
                        count += 1
                if count >= k:
                    ans = min(ans, (X[j] - X[i]) * (Y[m] - Y[l]))
print(ans)