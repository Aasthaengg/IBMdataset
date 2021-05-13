r,d,x2000=map(int,input().split())
xnow=x2000
for i in range(10):
  xnext = r*xnow - d
  print(xnext)
  xnow = xnext