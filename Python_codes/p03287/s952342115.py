import sys
from itertools import accumulate
from collections import Counter
n, m = [int(i) for i in sys.stdin.readline().split()]
a_ls = [int(i) for i in sys.stdin.readline().split()]
cumsum = [0] + [i % m for i in accumulate(a_ls)]
ct = Counter(cumsum)
res = 0
for k, v in ct.items():
    if v >= 2:
        res += v * (v-1) // 2
print(res)