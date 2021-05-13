n = int(input())
import math

for i in range(50000):
  if math.floor(i*1.08) == n:
    print(i)
    exit()
    
print(":(")