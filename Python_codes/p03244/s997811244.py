n = int(input())
V = list(map(int, input().split()))

import sys
from collections import Counter

C0 = Counter(V[0::2])
C1 = Counter(V[1::2])

n0 = C0.most_common()[0][0]
n1 = C1.most_common()[0][0]

minV = min(V)
if all([v == minV for v in V]):
    print(len(V)//2)
    sys.exit()

if n0 == n1:
    if C0.most_common()[1][1] >= C1.most_common()[1][1]:
        n0 = C0.most_common()[1][0]
    else:
        n1 = C1.most_common()[1][0]
    
count = 0
for v in V[0::2]:
    if v != n0:
        count += 1

for v in V[1::2]:
    if v != n1:
        count += 1
print(count)