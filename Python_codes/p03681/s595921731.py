n,m = map(int, input().split())

import math
mod = 10**9+7
if n==m:
    ans = math.factorial(n) * math.factorial(m) *2
    print(ans%mod)
elif abs(n-m)<2:
    ans = math.factorial(n) * math.factorial(m)
    print(ans%mod)
else:
    print(0)