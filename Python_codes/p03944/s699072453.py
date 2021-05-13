w,h,n=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
a=[0,w,0,h]
for i in range(n):
  if l[i][2]==1:
    a[0]=max(a[0],l[i][0])
  elif l[i][2]==2:
    a[1]=min(a[1],l[i][0])
  elif l[i][2]==3:
    a[2]=max(a[2],l[i][1])
  else:
    a[3]=min(a[3],l[i][1])
print(max(a[1]-a[0],0)*max(a[3]-a[2],0))