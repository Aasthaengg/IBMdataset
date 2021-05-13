n=int(input())
ans=[]
for i in range(1,n+1):
  for j in range(i+1,n+1):
    if i+j != n+int(n%2==0):
      ans.append((i,j))
print(len(ans))
for p in ans:
  x,y=p
  print(x,y)