from math import factorial
N = int(input())
power = factorial(N)
print(power % ((10**9) + 7))