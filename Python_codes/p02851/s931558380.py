from itertools import accumulate
from collections import Counter

N, K, *A = map(int, open(0).read().split())

S = [0] + [a % K for a in accumulate(a - 1 for a in A)]

C = Counter()
ans = 0
for i, s in enumerate(S):
    ans += C[s]
    C[s] += 1
    if i - K + 1 >= 0:
        C[S[i - K + 1]] -= 1

print(ans)