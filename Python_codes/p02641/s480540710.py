import sys

x,n = map(int, input().split())

if n == 0:
  print(x) 
  sys.exit()

p = set(map(int, input().split()))

if x not in p:
  print(x)

else:
  flag = True
  d = 0
  while flag == True:
    d += 1
    if x-d not in p:
      print(x-d)
      flag = False
    elif x+d not in p:
      print(x+d)
      flag = False
