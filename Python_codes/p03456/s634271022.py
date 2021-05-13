import math

a, b = input().split()
n1 = int(a + b)
n2 = int(math.sqrt(n1)) ** 2

print('Yes') if n1 == n2 else print('No')