import sys
A = []
for i in range(3):
  a,b = map(int,input().split())
  A.append(a)
  A.append(b)
if A.count(1) == 1:
  if A.count(4) == 1:
    if A.count(2) == 2:
      print("YES")
      sys.exit()
print("NO")