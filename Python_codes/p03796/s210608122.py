import math

N = int(input())

power = 1
power *= math.factorial(N)
power = power % (10**9 + 7)

print(power)