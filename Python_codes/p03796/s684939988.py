import math

N = int(input())
x = 10**9 + 7

ans = math.factorial(N)

print(ans % x)