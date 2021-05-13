N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10 ** 9 + 7

XS = 0
for i, x in enumerate(X, start=1):
    XS += (x * ((i - 1) - (N - i))) % mod
YS = 0
for i, y in enumerate(Y, start=1):
    YS += (y * ((i - 1) - (M - i))) % mod

print(XS * YS % mod)
