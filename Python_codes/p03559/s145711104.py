import sys
import bisect
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
b_ls = [int(i) for i in sys.stdin.readline().split()]
c_ls = [int(i) for i in sys.stdin.readline().split()]
a_ls.sort()
b_ls.sort()
c_ls.sort()
comb_a = []
comb_b = []
len_b = len(b_ls)
len_c = len(c_ls)
for a in a_ls:
    ind = len_b - bisect.bisect_right(b_ls, a)
    comb_a.append(ind)

prod_b = []
res = 0
for b in b_ls[::-1]:
    ind = len_c - bisect.bisect_right(c_ls, b)
    comb_b.append(ind)
    res += ind
    prod_b.append(res)
comb_b = comb_b[::-1]
_sum = 0
for a in comb_a:
    if a <= 0:
        continue
    _sum += prod_b[a-1]
print(_sum)