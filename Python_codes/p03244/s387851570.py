n = int(input())
v = list(map(int, input().split()))
from collections import Counter
odd_ary = v[::2]
even_ary = v[1::2]

# 最頻値top2
oc = Counter(odd_ary).most_common(2)
ec = Counter(even_ary).most_common(2)

if len(oc) == 1:
    oc.append((0, 0))
if len(ec) == 1:
    ec.append((0, 0))

if oc[0][0] != ec[0][0]:
    print(n - (oc[0][1] + ec[0][1]))
else:
    print(n - max(oc[0][1] + ec[1][1], oc[1][1] + ec[0][1]))
