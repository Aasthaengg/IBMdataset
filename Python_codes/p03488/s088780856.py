s = input().split("T")
x,y = map(int,input().split())
x -= len(s[0])
XY = [[],[]]
for i in range(1,len(s)):
  XY[i%2].append(len(s[i]))
X,Y = XY
X.sort(reverse = True)
Y.sort(reverse = True)
for i in X:
  if x > 0:
    x -= i
  else:
    x += i
for i in Y:
  if y > 0:
    y -= i
  else:
    y += i
if (x,y) == (0,0):
  print("Yes")
else:
  print("No")

