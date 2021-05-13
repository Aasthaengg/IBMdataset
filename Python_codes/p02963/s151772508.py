import math

N = int(input())
a = math.ceil(N/(10**9))
b = a*10**9-N
print(0, 0, 10**9, b, 1, a)