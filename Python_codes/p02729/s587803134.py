x,y = [int(x) for x in input().split()]
def c(m):
      if (m>=2):
            return m*(m-1)//2
      else:
            return 0
if (x<2 and y<2):
      print(0)
else:
      print(c(x)+c(y))
