n,m = map(int, input().split())
a = list(map(int, input().split()))
from itertools import accumulate
acc = [0] + [i % m for i in accumulate(a)]
from collections import Counter
ans = sum([v * (v-1) // 2 for v in Counter(acc).values()])
print(ans)