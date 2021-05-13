r,d,x = [int(y) for y in input().split()]

def getx(f):
      return r*f-d

for i in range(2001, 2011):
      x = getx(x)
      print(x)
