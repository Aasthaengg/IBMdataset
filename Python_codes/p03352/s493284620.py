x,l=int(input()),[0]*1001;l[1]=1
for i in range(2,int(x**0.5)+1):
  if l[i]==0:j=i*i
  while 1:
    if j>x:break
    else:l[j]=1;j*=i
for i in range(x,-1,-1):
  if l[i]==1:print(i);break