import sys
sys.setrecursionlimit(10**6)

n = int(input())
a2e = [int(input()) for _ in range(5)]

import math

neck = min(a2e)

ans = 5

t_neck = math.ceil(n/neck)

ans += t_neck-1

print(ans)