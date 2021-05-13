import math
a, b, n = map(int, input().split())
ans = []

def Calcf(i):
  return math.floor((a * i) / b) - a * math.floor(i / b)
    
print (Calcf(min(b - 1, n)))