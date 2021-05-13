m, n = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.sort()
Y.sort()
mod = 10**9 + 7
ax = 0
ay = 0
for ix, (x, x_) in enumerate(zip(X, X[::-1])):
    if x >= x_:
        break
    ax += ((x_ - x) % mod) * (m - 2 * ix - 1) % mod
    ax %= mod
for iy, (y, y_) in enumerate(zip(Y, Y[::-1])):
    if y >= y_:
        break
    ay += ((y_ - y) % mod) * (n - 2 * iy - 1) % mod
    ay %= mod
print(ax * ay % mod)