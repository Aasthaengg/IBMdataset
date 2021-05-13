import sys
from collections import Counter
n,t = [int(i) for i in sys.stdin.readline().split()]
a_ls = [int(i) for i in sys.stdin.readline().split()]
_max = 0
res = []
for a in a_ls[::-1]:
    _max = max(a, _max)
    res.append(_max - a)
ct = Counter(res)
print(ct[max(res)])
