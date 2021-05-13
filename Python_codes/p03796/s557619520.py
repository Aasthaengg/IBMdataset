import math
N = int(input())
a = math.factorial(N)
x = a % (10**9+7)
print(x)