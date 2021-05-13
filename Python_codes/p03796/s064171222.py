import math

N = int(input())

num = math.factorial(N)

k, r = divmod(num, 10**9 + 7)
print(r)