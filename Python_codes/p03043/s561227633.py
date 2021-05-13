import sys
input = lambda: sys.stdin.readline().rstrip()
from decimal import *

N, K = map(int, input().split())

x = Decimal("0.5")
ans = 0
for i in range(1, N+1):
    p = 1
    while i < K:
        i *= 2
        p *= x
    ans += p   
ans /= N
print(ans)