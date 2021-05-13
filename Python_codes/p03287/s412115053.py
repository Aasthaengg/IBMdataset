from itertools import accumulate
from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
S.extend(accumulate(A))
S = [s % M for s in S]

D = defaultdict(int)
ans = 0
for s in S:
    ans += D[s]
    D[s] += 1

print(ans)
