
def translate(W, a, b) : 
  if (a <= b <= a + W) or (a <= b + W <= a + W) :
    return 0
  else :
    if a <= b : 
      return b - (a + W)
    
    else : 
      return a - (b + W)


W, a, b = tuple(map(int, input().split()))

print(translate(W, a, b))