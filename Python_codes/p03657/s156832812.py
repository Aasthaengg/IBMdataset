import sys
a,b = map(int,input().split())
if (a+b)%3 == 0:
  print("Possible")
  sys.exit()
elif a%3 == 0:
  print("Possible")
  sys.exit()
elif b%3 == 0:
  print("Possible")
  sys.exit()
else:
  print("Impossible")