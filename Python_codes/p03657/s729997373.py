a, b = map(int, input().split())

def f(a):
  if a % 3 == 0:
    return True
  else:
    return False
  
if f(a) or f(b) or f(a + b):
  print("Possible")
else:
  print("Impossible")