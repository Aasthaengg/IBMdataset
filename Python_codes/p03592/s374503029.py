n,m,k=map(int,input().split())
ans=0
for i in range(0,n+1):
  for j in range(0,m+1):
    if m*i+(n-i*2)*j==k:
      ans=1
      break
  if ans==1:
    print("Yes")
    break
else:
  print("No")