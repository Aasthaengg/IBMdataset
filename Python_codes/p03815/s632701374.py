import math
x = int(input())
if x == 6 or (x-6)%11 == 0:
  x -= 1  
print(math.ceil(x/5.5))