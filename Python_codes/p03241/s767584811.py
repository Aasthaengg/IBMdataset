n, m = map(int, input().split())
# 素因数分解
from collections import defaultdict


def divide(n):  # unsort
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i == i:
                continue
            ans.append(n // i)
    return ans


ans = 1
soin = divide(m)
soin.sort(reverse=True)
for num in soin:
    if num * n <= m:
        ans = num
        break

print(ans)
