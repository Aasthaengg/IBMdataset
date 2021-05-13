import sys
x=int(input())
for a in range(-500,500):
  for b in range(-500,a):
    if x==pow(a,5)-pow(b,5):
      print(a)
      print(b)
      sys.exit()

