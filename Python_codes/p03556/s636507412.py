def isSquare(x):
  return x == round(x**(1/2))**2

N = int(input())
f = N
while True:
  if isSquare(f):
    print(f)
    exit()
  else:
    f -= 1