import sys
from collections import Counter
ct = Counter()
n, m = [int(i) for i in sys.stdin.readline().split()]
for i in range(m):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    ct.update([a, b])
if all([c % 2 == 0 for c in ct.values()]):
    print("YES")
else:
    print("NO")