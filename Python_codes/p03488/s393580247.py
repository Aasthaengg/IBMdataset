s = input().split("T")
x,y = map(int,input().split())
x-=len(s[0])
XY = [[],[]]

for n in range(1,len(s)):
  XY[n%2].append(len(s[n]))

X,Y = XY
X = sorted(X)[::-1]
Y = sorted(Y)[::-1]

for n in X:
  if 0<x:
    x-=n
  else:
    x+=n

for n in Y:
  if 0<y:
    y-=n
  else:
    y+=n

if (x,y)==(0,0):
  print("Yes")
else:
  print("No")