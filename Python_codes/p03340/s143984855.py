n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]=format(a[i],'022b')
A=[[0 for i in range(22)] for j in range(n+1)]
for i in range(n):
  for j in range(22):
    if a[i][j]=='1':
      A[i+1][j]=A[i][j]+1
    else:
      A[i+1][j]=A[i][j]

ct=0
right=1
for i in range(n):
  flag=0
  if i>right:
    right=i
  for j in range(right,n+1):
    check=0
    for k in range(22):
      if A[j][k]-A[i][k]<=1:
        check+=1
    if check!=22:
      right=j-1
      ct+=right-i
      flag=1
      break
  if flag==0:
    right=j
    ct+=right-i
print(ct)