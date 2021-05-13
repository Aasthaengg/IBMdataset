def count(l):
    res = {0:0, 1:0}
    for d in l:
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return res
from operator import mul
from functools import reduce

def cmb(n,r):
    if n < r: return 0
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n, p = map(int, input().split())
data = list(map(int, input().split()))
data = [i%2 for i in data]
oz = count(data)

ans = 0
m = 2**oz[0]
if p == 0:
    choice = 2
    ans += m
elif p == 1:
    choice = 1
ones = oz[1]
while choice <= ones:
    ans += m*cmb(ones, choice)
    choice += 2
print(ans)