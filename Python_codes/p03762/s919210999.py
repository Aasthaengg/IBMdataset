MOD = 1000000007
n, m = map(int,input().split())
xlst = list(map(int, input().split()))
ylst = list(map(int, input().split()))
xs = 0
for i in range(n - 1):
    w = xlst[i + 1] - xlst[i]
    xs += w * (i + 1) * (n - i - 1)
    xs %= MOD
ys = 0
for i in range(m - 1):
    h = ylst[i + 1] - ylst[i]
    ys += h * (i + 1) * (m - i - 1)
    ys %= MOD
print(xs * ys % MOD)