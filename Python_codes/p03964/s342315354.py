import sys
import math
n = int(input())
ls = []
for i in range(n):
    t, a = [int(i) for i in sys.stdin.readline().split()]
    ls.append((t, a))
_min = 1e-10
_min_a = 1
_min_t = 1
res = []
for l in ls:
    t, a = l
    _sum = t + a
    cnt = max(-(-_min_a//a), -(-_min_t//t))
    _min_a = cnt * a
    _min_t = cnt * t
    _min = cnt * _sum
    res.append(_min)
print(res[-1])