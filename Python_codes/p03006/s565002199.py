from collections import defaultdict
N = int(input())
if N == 1:
    print(1)
    exit()
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
d = defaultdict(int)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        p = X[i] - X[j]
        q = Y[i] - Y[j]
        d[(p, q)] += 1
print(N - max(d.values()))