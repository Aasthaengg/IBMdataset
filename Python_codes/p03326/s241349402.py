# https://atcoder.jp/contests/abc100/tasks/abc100_d
# https://www.hamayanhamayan.com/entry/2018/06/17/113721

from itertools import product

N, M = map(int, input().split())
X, Y, Z = [], [], []

for _ in range(N):
    xi, yi, zi = map(int, input().split())
    X.append(xi)
    Y.append(yi)
    Z.append(zi)

# +1/-1で全探索
ans = -1
for a, b, c in product([-1, 1], [-1, 1], [-1, 1]):
    v = [a * X[i] + b * Y[i] + c * Z[i] for i in range(N)]
    v.sort(reverse=True)
    ans = max(ans, sum(v[:M]))
print(ans)