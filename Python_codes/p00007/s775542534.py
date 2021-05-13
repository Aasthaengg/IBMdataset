from math import ceil
s = 100000
n = int(input())
for i in range(n):
   s = s + s*0.05
   s = ceil(s/1000)*1000

print(s)
