from operator import itemgetter

inf = 10 ** 4

n, m = map(int, input().split())
a = tuple(map(int, input().split()))

use = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# use[i] : 数字iを作るのに必要なマッチの本数

use_num = {use[i]: i for i in range(1, 10) if i in a}
use_num = tuple(sorted(use_num.items()))
# 本数昇順
# print(use_num)

dp = [-inf] * (n + 1)
dp[0] = 0
# dp[j] : j本から構成できる桁数の最大値

for j in range(2, n + 1):
    for use, number in use_num:
        k = j - use
        if k >= 0:
            dp[j] = max(dp[j], dp[k] + 1)
# print(dp)

use_num = tuple(sorted(use_num, key=itemgetter(1), reverse=True))
# 数字降順

rest = n
ans = ''
while rest > 0:
    for use, number in use_num:
        k = rest - use
        if (k >= 0) and (dp[k] == dp[rest] - 1):
            ans += str(number)
            rest -= use
            break
print(ans)