from collections import Counter
import numpy as np
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
n, m = map(int, input().split())
lst = list(map(int, input().split()))
blst = [0]
total = 0
for i in range(n):
    total += lst[i]
    blst.append(total)
modblst = np.array(blst)%m
count = Counter(modblst)

ans = 0
for val in count.values():
    if val == 1:
        continue
    ans += cmb(val, 2)
print(ans)