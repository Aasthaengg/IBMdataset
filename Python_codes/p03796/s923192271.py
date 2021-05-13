import math
num = int(input())
result = math.factorial(num) % (10 ** 9 + 7)
print(result)