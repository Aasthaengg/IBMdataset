import math

n = int(input())
prime = n

for i in range(n):
    num = int(input())
    for j in range(2,int(math.sqrt(num)+1)):
      if num % j == 0:
       prime -= 1
       break

print(prime)