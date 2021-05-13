import math
N = int(input())
N = math.factorial(N)
N = (N % (1000000000+7))
print(N)