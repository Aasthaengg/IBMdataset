from math import gcd
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
d = list(range(max_a+1))
for i in range(2, int(max_a**0.5)+1):
    if d[i] == i:
        for k in range(2*i, max_a+1, i):
            if d[k] == k:
                d[k] = i

exist = [0] * len(d)
res = 'pairwise coprime'
for i in range(n):
    val = a[i]
    s = set()
    while val != 1:
        s.add(d[val])
        val //= d[val]

    for k in s:
        if exist[k]:
            res = 'setwise coprime'
            break
        exist[k] = 1
    else:
        continue
    break

if res == 'setwise coprime':
    if reduce(gcd, a) != 1:
        res = 'not coprime'

print(res)
