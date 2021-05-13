import math
a, b, n = map(int, input().split())
 
 
def calc(a, b, n):
    return int(math.floor((a * n)/b) - (a * math.floor(n/b)))
 
if n <= b -1:
  print(calc(a,b,n))
else:
  print(calc(a,b,b-1))