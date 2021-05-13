n=int(input())
a=list(map(int,input().split()))
temp=[0,0,0,0,0,0,0,0]
r=0
for i in range(n):
  if a[i]>=3200:
    r=r+1
  elif a[i]>=2800:
    temp[7]=1
  elif a[i]>=2400:
    temp[6]=1
  elif a[i]>=2000:
    temp[5]=1
  elif a[i]>=1600:
    temp[4]=1
  elif a[i]>=1200:
    temp[3]=1
  elif a[i]>=800:
    temp[2]=1
  elif a[i]>=400:
    temp[1]=1
  else:
    temp[0]=1
if sum(temp)==0:
  print(1,r)
else:
  print(sum(temp),sum(temp)+r)  