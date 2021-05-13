import math
N, M = map(int, input().split())
from collections import*
c = Counter(map(int, input().split()))
for _ in range(M):
    B, C = map(int, input().split())
    c[C] = c[C] + B if C in c else B
c = sorted(c.items(), reverse=True)
s = 0
for i in c:
    s += i[0] * min(i[1],N)
    N -= min(i[1],N)
print(s)
