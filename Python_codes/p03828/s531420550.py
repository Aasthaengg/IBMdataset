import math
from collections import defaultdict

N = int(input())
mod = 10 ** 9 + 7
ans = 1
# それぞれの因数となる素数の数をセットする
dp = [0] * (N + 1)
# 素因数分解する関数
def prime_factorize(n):
    divisors = []
    # 27(2 * 2 * 7)の7を出すためにtemp使う
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                # 素因数を見つけるたびにtempを割っていく
                temp //= i
            divisors.append([i, cnt])
    if temp != 1:
        divisors.append([temp, 1])
    if divisors == []:
        divisors.append([n, 1])

    return divisors

for i in range(1, N + 1):
    for j in prime_factorize(i):
        if j[0] > 1:
            dp[j[0]] += j[1]
# 約数の数:それぞれの因数の(因数の数 + 1)を掛け合わせたもの
for i in dp:
    if i > 0:
        ans = (ans * (i + 1)) % mod
print(ans % mod)
