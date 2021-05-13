import itertools
N, M = map(int, input().split())
X, Y, Z = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

ans = 0
for a, b, c in itertools.product([-1, 1], repeat=3):
    tmp = []
    for x, y, z in zip(X, Y, Z):
        tmp.append(a * x + b * y + c * z)
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:M]))

print(ans)
