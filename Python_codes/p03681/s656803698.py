n,m = map(int,input().split())
ans = 0

import math

if n == m:
    ans = (math.factorial(n)%(10**9+7)) * (math.factorial(m)%(10**9+7)) * 2
    
elif abs(n-m) == 1:
    ans = (math.factorial(n)%(10**9+7)) * (math.factorial(m)%(10**9+7))
    
print(ans%(10**9+7))