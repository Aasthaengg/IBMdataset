wmax,hmax,n=map(int,input().split())
wmin,hmin=0,0
for i in range(n):
  x,y,a=map(int,input().split())
  if a==1:
    wmin=max(wmin,x)
  elif a==2:
    wmax=min(wmax,x)
  elif a==3:
    hmin=max(hmin,y)
  elif a==4:
    hmax=min(hmax,y)

if hmin>=hmax or wmin>=wmax:
  print(0)
else:
  print((hmax-hmin)*(wmax-wmin))
