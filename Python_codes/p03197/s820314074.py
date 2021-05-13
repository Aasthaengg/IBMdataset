n=int(input())
arr=[int(input()) for _ in range(n)]
cnt=0
flag=0
for i in range(n):
  if arr[i]==1:
    cnt+=1
  else:
    if arr[i]%2==1:
      flag=1
if cnt==0:
  if flag==0:
    print('second')
  else:
    print('first')
else:
  print('first')