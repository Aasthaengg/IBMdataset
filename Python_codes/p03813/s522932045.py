import sys
operaciones = list()
p=0
lines = sys.stdin.readlines()
for linea in lines:
    c = linea.split()
    c = list(map(int,c))
list(c)
x = c[0]
if x>= 1200:
  print("ARC")
elif x<1200:
  print("ABC")