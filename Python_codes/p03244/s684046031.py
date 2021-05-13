import sys
from collections import Counter

N = int(input())
V = list(map(int, sys.stdin.readline().rsplit()))

Ceven = Counter(V[::2])
Codd = Counter(V[1::2])

res = 0
even, odd = Ceven.most_common(2), Codd.most_common(2)
if even[0][0] != odd[0][0]:
    res = N - even[0][1] - odd[0][1]
else:
    if len(Ceven) == len(Codd) == 1:
        res = N // 2
    else:
        res = min(
            N - even[1][1] - odd[0][1],
            N - even[0][1] - odd[1][1]
        )
print(res)
