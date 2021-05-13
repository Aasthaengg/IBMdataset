import math
a,b = input().split()
number = int(a + b)

sqrtNumber = math.sqrt(number)

print("Yes") if int(sqrtNumber) == sqrtNumber else print("No")