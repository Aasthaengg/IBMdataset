import sys
import math
N = int(sys.stdin.readline().rstrip())

# def create_money(i):
#     money = []
#     tmp = 1
#     for _ in range(math.floor(math.log(N, i))):
#         tmp *= i
#         money.append(tmp)
    
#     return money

# money = [1]
# money += create_money(6)
# money += create_money(9)

money = [1]
for i in range(20):
    if 100000 >= 6**i:
        money.append(6**i)
    if 100000 >= 9**i:
        money.append(9**i)

money = sorted(money)[::-1]


dp = [[10**18] * (N + 1) for _ in range(len(money) + 1)]
dp[0][0] = 0

for i in range(1, len(money) + 1):
    m = money[i - 1]
    for j in range(N + 1):
        if j - m >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - m] + 1, dp[i][j - m] + 1)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[len(money)][N])