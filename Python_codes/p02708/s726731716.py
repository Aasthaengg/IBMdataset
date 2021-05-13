from itertools import accumulate

n, k = map(int, input().split())
MOD = 10 ** 9 + 7
acc = [0] + list(accumulate(range(n + 1)))

ans = 0
for i in range(k, n + 2):
    mi = acc[i]
    ma = acc[-1] - acc[-i - 1]
    ans += ma - mi + 1
    ans %= MOD

print(ans)