from itertools import accumulate
from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(accumulate([0]+A, lambda acc, a: (acc+a)%M))
ans = 0
S = defaultdict(int)
for b in B:
    ans += S[b]
    S[b] += 1
print(ans)