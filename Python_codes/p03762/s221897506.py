from itertools import accumulate

n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10 ** 9 + 7
# X.sort()
# Y.sort()
AX = list(accumulate([0] + X))
AY = list(accumulate([0] + Y))
xsum = 0
for i in range(1, n):
    xsum += (AX[n] - AX[i]) - (n - i) * X[i - 1]
    xsum %= mod
ysum = 0
for i in range(1, m):
    ysum += (AY[m] - AY[i]) - (m - i) * Y[i - 1]
    ysum %= mod
ans = xsum * ysum
print(ans % mod)
