n=int(input())
E=[]
if n%2==0:
  s=n+1
else:
  s=n
for i in range(1,n):
  for j in range(i+1,n+1):
    if i+j==s:
      continue
    else:
      E.append((i,j))
print(len(E))
for i,j in E:
  print(i,j)