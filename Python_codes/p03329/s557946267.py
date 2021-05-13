N = int(input())

def drawal(x):
  if(x <= 5):
    return x
  elif(6<= x and x < 9):
    return x- 5
  elif(9<= x and x < 15):
    return x- 8
  else:
    def drawal9(y):
      i = 0
      while 9** (i+ 1)<= y:
        i+= 1
      return drawal(y- 9** i)+ 1
    def drawal6(z):
      i = 0
      while 6** (i+ 1)<= z:
        i+= 1
      return drawal(z- 6** i)+ 1
    return min(drawal9(x), drawal6(x))

print(drawal(N))