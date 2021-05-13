# nを素因数分解したリストを返す
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

n = int(input())

from collections import defaultdict
dic = defaultdict(int)

for i in range(1, n+1):
    for prime in prime_decomposition(i):
        dic[prime] += 1

values = dic.values()

up2 = 0
up4 = 0
up14 = 0
up24 = 0
up74 = 0
for d in values:
    if d >= 74:
        up74 += 1
    if d >= 24:
        up24 += 1
    if d >= 14:
        up14 += 1
    if d >= 4:
        up4 += 1
    if d >= 2:
        up2 += 1

# 5 * 5 * 3
# 25 * 3
# 15 * 5
# 75

ans = 0
#75
ans += up74
#25*3
ans += up24 * (up2 - 1)
#15*5
ans += up14 * (up4 - 1)
#5*5*3
ans += up4 * (up4 - 1) * (up2-2) // 2


print(ans)
