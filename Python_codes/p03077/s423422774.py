import math

n=int(input())
li=[int(input()) for _ in range(5)]
div=n

for l in li:
  if l < div:
    div = l
    
print(math.ceil(n/div)+4)