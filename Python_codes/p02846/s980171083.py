t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
v1 = [a1,b1]
d = a1*t1 + a2*t2 - b1*t1 - b2*t2
if d == 0:
  print("infinity")
  exit()
if d > 0:
  f = 0
  s = 1
else:
  f = 1
  s = 0
  d = -d
l = t1*(v1[s]-v1[f])
if l < 0:
  print(0)
  exit()
tm = int(l//d)
if int(l%d) == 0:
  print(2*tm)
else:
  print(1+2*tm)