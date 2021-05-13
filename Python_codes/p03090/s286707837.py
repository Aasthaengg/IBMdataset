n=int(input())
ans=[]
if n%2==1:
  for i in range((n-1)//2):
    for j in range(i+1,n-i):
      if i==0:
        ans.append(((n-i),j))
      else:
        ans.append((i,j))
        ans.append(((n-i),j))
elif n%2==0:
  for i in range(1,n//2):
    for j in range(i+1,n-i+1):
      ans.append((i,j))
      ans.append(((n-i+1),j))
print(len(ans))
for u,v in ans:
  print(u,v)