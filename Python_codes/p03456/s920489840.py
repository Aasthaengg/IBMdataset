import math

a, b = map(str, input().split())
num = int(a+b)
print('Yes') if int(math.sqrt(num))**2 == num else print('No')