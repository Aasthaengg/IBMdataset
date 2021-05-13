import math
n,m = map(int,input().split())

x = 10**9+7

ans = 0
if n == m:
    ans += math.factorial(n) * math.factorial(m) * 2
    print(ans % x)
    exit()
elif n >= m and n -m == 1:
    ans += math.factorial(n) * math.factorial(m)
    print(ans % x)
    exit()
elif m >= n and m -n== 1:
    ans += math.factorial(n) * math.factorial(m)
    print(ans % x)
    exit()
else:
    print(ans % x)