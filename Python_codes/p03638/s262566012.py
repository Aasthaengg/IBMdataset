h,w=map(int,input().split())
n=int(input())
a=[0]+list(map(int,input().split()))
c=[[0]*w for _ in range(h)]
g=[0,w-1][h%2]
x,y=0,0
i=1
while True:
  c[x][y]=i
  a[i]-=1
  if x==h-1 and y==g:break
  if a[i]==0:i+=1
  if x%2:
    if y:y-=1
    else:x+=1
  else:
    if y==w-1:x+=1
    else:y+=1
for i in c:
  print(*i)