n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
  temp=list(map(str,input()))
  a.append(temp)
for i in range(m):
  temp=list(map(str,input()))
  b.append(temp)
temp=[]
ans=0
for i in range(n-m+1):
  for j in range(n-m+1):
    count=0
    for k in range(m):
      for l in range(m):
        if b[k][l]==a[k+i][l+j]:
          count=count+1
    if count==m*m:
      ans=1
if ans==1:
  print("Yes")
else:
  print("No")