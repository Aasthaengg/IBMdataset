import math
n = int(input())
a = min(math.factorial(n), math.factorial(n)%(10**9+7))
print(a)