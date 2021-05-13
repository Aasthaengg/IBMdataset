import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

d = defaultdict(int)

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    d[s] += 1

# print(d)
d2 = sorted([(v, k) for k, v in d.items()])
m = max(d2)[0]  # v の回数で max を拾う
# print(m)
for v, k in d2:
    if v == m:
        print(k)
