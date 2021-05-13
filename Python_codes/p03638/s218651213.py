h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
  l+=[i+1]*a[i]
ans=[[0]*w for i in range(h)]
idx=0
for i in range(h):
  if i%2==0:
    for j in range(w):
      ans[i][j]=l[idx]
      idx+=1
  else:
    for j in range(w)[::-1]:
      ans[i][j]=l[idx]
      idx+=1
for i in range(h):
  print(*ans[i])