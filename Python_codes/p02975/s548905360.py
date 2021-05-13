#!/usr/bin/env python3
from collections import Counter

n = int(input())
(*a, ) = map(int, input().split())
c = Counter(a)
b = 0
for i in c.keys():
    b ^= i
if sum(a) == 0 or (b == 0 and all(i * 3 == n for i in c.values())):
    print("Yes")
elif len(c) == 2 and c.most_common()[0][1] * 3 == 2 * n and c.most_common(
)[1][0] == 0:
    print("Yes")
else:
    print("No")
