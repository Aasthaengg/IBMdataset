N, D = map(int, input().split())
X = list()
Y = list()
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count = 0
for i in range(N):
    if X[i] * X[i] + Y[i] * Y[i] <= D * D:
        count += 1

print(count)
