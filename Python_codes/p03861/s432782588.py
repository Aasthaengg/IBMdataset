
def ans() : 
  a, b, x = tuple(map(int, input().split()))
  c1 = b // x
  c2 = (a - 1) // x
  print(c1 - c2)
  
  
ans()