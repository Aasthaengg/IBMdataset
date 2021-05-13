import sys
from collections import Counter
ct = {i:0 for i in range(1,5)}
for i in range(3):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    ct[a] += 1
    ct[b] += 1
ct2 = Counter(ct.values())
if ct2[1] == 2 and ct2[2] == 2:
    print("YES")
else:
    print("NO")