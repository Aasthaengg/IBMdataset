h,w=map(int,input().split())
a=[]
for _ in range(h):
  s=list(input())
  a.append(s)

ch1=0

for x in range(h):
  for y in range(w):
    b=a[x][y]
    ch=0
    if b=='#':
      if 0<=x-1<=h-1 and a[x-1][y]=='#':
        ch+=1
      if 0<=x+1<=h-1 and a[x+1][y]=='#':
        ch+=1
      if 0<=y-1<=w-1 and a[x][y-1]=='#':
        ch+=1
      if 0<=y+1<=w-1 and a[x][y+1]=='#':
        ch+=1
      
      if ch==0:
        ch1+=1
   
  
if ch1==0:
  print('Yes')
else:
  print('No')
