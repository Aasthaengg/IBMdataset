import math

N = int(input())
lists = [ int(v) for v in input().split(" ") ]

total = 0

for l in lists:
  if l % 2 == 0:
    while True:
      if l % 2 == 0:
        l = int(l/2)
        total += 1      
      else:
        break
print(total)