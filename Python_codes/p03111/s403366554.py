n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]
targets = [a, b, c]

ans = 10**9
from itertools import product
for comb in product([0, 1, 2, 3], repeat=n):
    if len(set(comb)) in [1, 2]:
        continue
    # a, b, c
    ls = [[], [], []]
    for i, c in enumerate(comb):
        if c == 3:
            continue
        ls[c].append(L[i])

    mps = 0
    for idx, ll in enumerate(ls):
        if len(ll) == 0:
            break
        tmp = (len(ll)-1)*10
        mps += tmp
        mps += abs(targets[idx] - sum(ll))
    else:
        ans = min(ans, mps)
    
print(ans)
