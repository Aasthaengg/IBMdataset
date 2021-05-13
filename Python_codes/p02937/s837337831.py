s=input()
t=input()
ls=len(s)
alpha="abcdefghijklmnopqrstuvwxyz"
c={}
l={}
for i in alpha:
  c[i]=[]
  l[i]=0
  
for i in range(ls):
  c[s[i]].append(i)
  l[s[i]]+=1

f=True
x,y=0,-1
for i in t:
  if l[i]==0:
    f=False
    break
  left,right=-1,l[i]
  while right-left!=1:
    a=(left+right)//2
    if c[i][a]>y:
      right=a
    else:
      left=a
  if right==l[i]:
    x+=1
    y=c[i][0]
  else:
    y=c[i][right]
if f:
  print(x*ls+y+1)
else:
  print(-1)