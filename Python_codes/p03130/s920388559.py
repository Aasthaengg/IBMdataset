a=[0,0,0,0]
for i in range(3):
  x,y=map(int,input().split())
  a[x-1]+=1
  a[y-1]+=1
b=1
for i in range(4):
  if a[i]==3:
    print("NO")
    b=0
    break
if(b):
  print("YES")