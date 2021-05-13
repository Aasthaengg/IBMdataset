from collections import Counter
N,A,B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

c = Counter(v)
ans_num = sum(v[:A]) / A
ans_cnt = 0

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

num = v[A-1]
num_all = c[num]
cc = Counter(v[:A])
tmp = cc[num]

for i in range(A-1, B):
    last = v[i]
    if i != A-1:
        if last != v[0]:
            break
    ans_cnt += cmb(num_all, (i+1)-(A-tmp))


print(ans_num)
print(ans_cnt)
