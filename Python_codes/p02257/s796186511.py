import sys
import math

def isPrime(x):
     if x <= 1:
          return False
     if x == 2:
          return True
     root_x = int(math.sqrt(x)) + 1
     for num in range(2, root_x):
          if x%(num) == 0:
               return False
     return True

input = []
for line in sys.stdin:
     input.append(int(line))
##input = [2, 4, 7, 1, 2, 3, 1, 11, 4576435353, 2342342]
count = 0
for num in set(input):
     if isPrime(num):
          count += 1

print count