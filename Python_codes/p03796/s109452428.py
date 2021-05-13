import math
  
n = int(input())
result = math.factorial(n)
  
  
dividor = 10 ** 9 + 7
print (result % dividor)