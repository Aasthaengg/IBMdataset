import math
of = 10**9+7
n,m = map(int,input().split())
if abs(n-m) >= 2:
    print(0)
    exit()
if n == m:
    print(math.factorial(n)*math.factorial(m)*2 % of)
else:
    print(math.factorial(n)*math.factorial(m) % of)