import sys
from collections import Counter

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

n = ni()
v = nl()
odd = Counter(v[0::2])
even = Counter(v[1::2])
odd["$"] = 0
even["#"] = 0
ans = 0
if odd.most_common()[0][0] == even.most_common()[0][0]:
    if odd.most_common()[1][1] > even.most_common()[1][1]:
        ans = n - odd.most_common()[1][1] - even.most_common()[0][1]
    else:
        ans = n - odd.most_common()[0][1] - even.most_common()[1][1]
else:
    ans = n - odd.most_common()[0][1] - even.most_common()[0][1]
"""if len(odd) == 1:
    pass
else:
    for v in odd.values():
        max_odd = max(max_odd, v)
    ans += len(odd) - max_odd

if len(even) == 1:
    pass
else:
    for v in even.values():
        max_even = max(max_even, v)
    ans += len(even) - max_even"""

print(ans)