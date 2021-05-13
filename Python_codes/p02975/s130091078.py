N = int(input())
A = list(map(int, input().split()))

import sys
from collections import Counter
d = Counter(A)

if d[0] == N:
    print("Yes")
    sys.exit()

if d[0] == N // 3:
    for x in d.keys():
        if d[x] == 2 * N // 3:
            print("Yes")
            sys.exit()

third = N // 3
if len(d.keys()) == 3:
    a, b, c = d.keys()
    if d[a] == d[b] and d[b] == d[c]:
        if a ^ b ^ c == 0:
            print("Yes")
            sys.exit()

print("No")