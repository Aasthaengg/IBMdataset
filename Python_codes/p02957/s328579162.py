x,y = [int(a) for a in input().split()]

if ((x+y)%2 == 1):
      print("Impossible".upper())
else:
      print((x+y)//2)
