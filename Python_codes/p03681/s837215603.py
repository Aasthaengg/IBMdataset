# C - Reconciled?
import math
N, M = map(int,input().split())

S = math.factorial(min(N,M)) % 1000000007

ans = 0
if abs(N-M) > 1:
    ans = 0
elif abs(N-M) == 1:
    ans = S*S*max(N,M)
else:
    ans = S*S*2

ans = ans % 1000000007

print(ans)
