from collections import defaultdict
import collections
import sys
input = sys.stdin.readline

n, K = [int(w) for w in input().split()]
dd = collections.defaultdict(int)

for i in range(n):
    a, b = [int(w) for w in input().split()]
    dd[a] += b

s_dd = sorted(dd.items(), key=lambda x: x[0])

i = 0
ans = 0
for k, v in s_dd:
    i += v
    if i >= K:
        ans = k
        break
print(ans)
