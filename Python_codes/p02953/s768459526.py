n=int(input())
h=list(map(int,input().split()))
flag=False
h[0]-=1

for i in range(1,n):
  if h[i-1]<=h[i]-1:
    h[i]-=1
  elif h[i-1]==h[i]:
    pass
  else:
    flag=True
    break
    
if flag:
  print('No')
else:
  print('Yes')