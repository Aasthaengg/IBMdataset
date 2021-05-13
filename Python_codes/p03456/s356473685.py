from math import sqrt

def isSquare(n):
  return n == pow(round(sqrt(n)),2)

n = int(input().replace(" ",""))
if isSquare(n):
  print("Yes")
else:
  print("No")