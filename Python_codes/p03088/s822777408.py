from itertools import product
from collections import defaultdict
MOD = 10**9 + 7
N = int(input())
D, L = 4, 3
AGC = list(range(L))
ATGC = range(D)
cur = defaultdict(lambda: 1)
# XAGC, XGAC, AXGC, AGXC, XACG: prohibited
flip = lambda x, n: x[:n] + [x[n+1],x[n]] + x[n+2:]
prohibited1 = [tuple(AGC)] + [tuple(flip(AGC,i)) for i in range(L-1)]
prohibited2 = ({(X,) + p for p in prohibited1 for X in ATGC} | 
             {tuple(flip([X]+AGC,0)) for X in ATGC} |
             {tuple(flip(AGC+[X],L-1)) for X in ATGC})
for p in prohibited1:
    cur[p] = 0
for _ in range(L,N):
    prev = cur
    cur = defaultdict(int)
    for recent in product(ATGC, repeat=L+1):
        if recent in prohibited2:
            continue
        else:
            cur[recent[1:]] += prev[recent[:-1]]
    for latest in product(ATGC, repeat=L):
        cur[latest] %= MOD

ans = sum(cur.values()) % MOD
if N < L:
    print(D**N)
elif N == L:
    print(D**L - len(prohibited1))
else:
    print(ans)