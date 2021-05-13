n = int(input())
S = list(input())

# aを含む -> 個数通り 含まない-> 1
# bを含む -> 個数通り 含まない-> 1
from collections import defaultdict
d = defaultdict(int)
for s in S:
    d[s] += 1
ans = 1
mod = 10**9 + 7
for k in d.keys():
    ans *= (d[k]+1)
    ans %= mod
ans -= 1
print(ans)