import math
N = int(input())
TAX = 1.08
a = math.ceil(N / TAX)
print(a) if math.floor(a * TAX) == N else print(":(")