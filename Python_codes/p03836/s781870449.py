sx,sy,gx,gy=map(int,input().split())
s=''
t=''
for i in range(gx-sx):
  s+='R'
  t+='L'
for i in range(gy-sy):
  s+='U'
  t+='D'
s+=t
s+='D'
t='U'
for i in range(gx-sx+1):
  s+='R'
  t+='L'
for i in range(gy-sy+1):
  s+='U'
  t+='D'
s+='L'+t+'R'
print(s)