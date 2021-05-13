import sys
import math

max = 10**9+7
n,m = map(int,input().split())
ans = 0

if n+1 < m or m+1 < n:
    print(0)
    sys.exit()

if n == m:
    ans = ((math.factorial(n))*(math.factorial(m)))*2
else:
    ans = (math.factorial(n))*(math.factorial(m))

print(ans%max)