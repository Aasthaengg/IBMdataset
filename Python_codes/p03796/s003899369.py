import math
N = int(input())
n = 10**9 + 7
power = math.factorial(N)
print(power % n)