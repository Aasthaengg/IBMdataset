N, M = map(int, input().split())
A = map(int, input().split())
from itertools import accumulate
from collections import Counter
acc = [0]
acc.extend(accumulate(A))
cnt = Counter(a % M for a in acc)
ans = sum(v * (v - 1) // 2 for v in cnt.values())
print(ans)