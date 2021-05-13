import sys
N, R = map(int, input().split())

cond = (N <= 10)
ans = R + 100 * (10-N) if cond else R

print(ans)