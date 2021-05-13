N, M = map(int, input().split())
from collections import*
c = Counter(map(int, input().split()))
for _ in range(M):
    B, C = map(int, input().split())
    c[C] = c[C] + B if C in c else B
s = 0
for i in sorted(c.items())[::-1]:
    m = min(i[1], N)
    s += i[0] * m
    N -= m
print(s)
