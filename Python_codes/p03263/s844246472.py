import sys

#input=sys.stdin.readline
h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
d=[]
for i in range(h):
    for j in range(w):
        if a[i][j]%2==1:
             d.append((i,j))
n=len(d)
if n==0:
  print(0)
  exit()
d_s=set(d)
ans=[]
f=False
y=d[0][0]
x=d[0][1]
xp=x+1
yp=y
while True:
    if y%2==0:
      xp=x+1
    else:
      xp=x-1
    yp=y
    if (y,x) in d_s:
      while True:
          if (yp,xp) not in d_s and -1<xp<w and yp<h:
              if yp%2==0:
                  ans.append([y+1,x+1,yp+1,xp+1])
                  x=xp
                  xp+=1
              else:
                  ans.append([y+1,x+1,yp+1,xp+1])
                  x=xp
                  xp-=1
              y=yp
          elif (yp,xp) not in d_s and xp>w-1:
              xp=w-1
              yp+=1
          elif (yp,xp) not in d_s and xp<0:
              xp=0
              yp+=1
          elif (yp,xp) in d_s:
              ans.append([y+1,x+1,yp+1,xp+1])
              if yp%2==0:
                x=xp+1
                y=yp
              else:
                x=xp-1
                y=yp
              break
          elif yp>h-1:
            f=True
            break
      if f:
        break
    else:
      if y%2==0:
        x+=1
      else:
        x-=1
      if x>w-1:
        x=w-1
        y+=1
      elif x<0:
        x=0
        y+=1
    if y>h-1:
      break
print(len(ans))
for i in ans:
  print(*i)