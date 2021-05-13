n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
pin=a[0]
cnt=1
x=[]
for i in range(1,n):
  if a[i]==pin and i!=(n-1):
    cnt+=1
  elif a[i]!=pin:
    if cnt>=4:
      x+=[pin]
      x+=[pin]
    elif cnt>=2:
      x+=[pin]
    if len(x)>=2:
      break
    pin=a[i]
    cnt=1
  
  elif i==(n-1):
    if pin==a[i]:
      cnt+=1
    if cnt>=4:
      x+=[pin]
      x+=[pin]
    elif cnt>=2:
      x+=[pin]
    if len(x)>=2:
      break
    pin=a[i]
    cnt=1

    
if len(x)<=1:
  print(0)
else:
  print(x[0]*x[1])
