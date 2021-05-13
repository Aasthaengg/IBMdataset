sx,sy,gx,gy=map(int,input().split())
s,t,u,v='','','DR','UL'
for i in range(gx-sx):
  s+='R'
  t+='L'
  u+='R'
  v+='L'
u+='U'
v+='D'
for i in range(gy-sy):
  s+='U'
  t+='D'
  u+='U'
  v+='D'
print(s+t+u+'L'+v+'R')