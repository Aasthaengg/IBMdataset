n=int(input())
a=list(map(int,input().split()))
ans=999999999999999
temp=True
for i in range(2):
  count=0
  temp=0
  if i==0:
    t=True
  else:
    t=False
  for j in a:
    temp=temp+j
    if t==True and temp<1:
      count=count+1-temp
      temp=1
    elif t==False and temp>-1:
      count=count+1+temp
      temp=-1
    if t==True:
      t=False
    else:
      t=True
  ans=min(ans,count)
print(ans)