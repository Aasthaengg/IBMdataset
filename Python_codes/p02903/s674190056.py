h,w,a,b=map(int,input().split())
a-=1
b-=1
ans=[[0 for i in range(w)] for j in range(h)]
for i in range(h):
  for j in range(w):
    if (i>b and j>a) or (i<=b and j<=a):
      ans[i][j]=1
for x in ans:
  print(*x,sep="")