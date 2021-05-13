# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b

n = int(input())
X, Y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    X.append(xi)
    Y.append(yi)
# print(X)
# print(Y)

if n == 1:
    print(1)
    exit()

# PQをバラすとだめ？
posPQ = []
score = int(1e18)
for i in range(n):
    xi, yi = X[i], Y[i]
    for j in range(n):
        if i == j:
            continue
        xj, yj = X[j], Y[j]
        p = xj - xi
        q = yj - yi

        # posPQ.append((dx, dy))
        count = n
        for k in range(n):
            for l in range(n):
                if X[l] - X[k] == p and Y[l] - Y[k] == q:
                    count -= 1
        # print(p, q, count)
        score = min(score, count)
print(score)