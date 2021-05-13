n=int(input())
a=list(map(int,input().split()))
b=[0]*9
while a:
  kazu=a.pop(0)
  if 1<=kazu < 400:
    b[0]=1
  elif kazu < 800:
    b[1]=1
  elif kazu < 1200:
    b[2]=1
  elif kazu < 1600:
    b[3]=1
  elif kazu < 2000:
    b[4]=1
  elif kazu < 2400:
    b[5]=1
  elif kazu < 2800:
    b[6]=1
  elif kazu < 3200:
    b[7]=1
  elif kazu >=3200:
    b[8]+=1
coma=b[8]
comi=0
for i in b[:8]:
  if i > 0:
    comi+=1
if coma > 0 and comi ==0:
  comi =1
if comi+coma >= n:
  maxgo=n
else:
  maxgo=comi+coma
print(comi,maxgo)