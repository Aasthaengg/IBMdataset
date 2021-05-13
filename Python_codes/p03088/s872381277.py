import sys
N = int(sys.stdin.readline().rstrip())
mod = 10**9+7

from collections import defaultdict
from itertools import product

A = [('A','G','C'),('G','A','C'),('A','C','G')]

for i in range(3,N+1):
    if i == 3:
        d = defaultdict(int)  # d[a] = aで終わる条件を満たす文字列の個数
        for a in list(product(['A','C','G','T'],repeat=3)):
            d[(a[0],a[1],a[2])] = 1
        for a in A:
            d[a] = 0
    else:
        new_d = defaultdict(int)
        for a in ['A','C','G','T']:
            for b in list(product(['A','C','G','T'],repeat=3)):
                if not ((b[1],b[2],a) in A or (b[0],b[1],a) == ('A','G','C') or (b[0],b[2],a) == ('A','G','C')):
                    new_d[(b[1],b[2],a)] += d[b]
                    new_d[(b[1], b[2], a)] %= mod
        d = new_d

print(sum(d.values()) % mod)