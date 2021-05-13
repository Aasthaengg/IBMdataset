import sys
r = []
n = int(input())
l = sys.stdin.readlines()
for i in l:
  x, y, z = sorted(map(lambda x:x*x,map(int, i.split())))
  if x + y == z:
      print("YES")
  else:
      print("NO")