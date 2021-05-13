import math
N, M = map(int, input().split())
ans = 0
if abs(N-M) == 0:
    ans = 2*math.factorial(N)**2
elif abs(N-M) == 1:
    ans = math.factorial(N)*math.factorial(M)
print(ans%(10**9+7))
