n,k=map(int,input().split())
m=(n-1)*(n-2)/2
ans=[]
if m<k:
  print(-1)
  exit()
else:
  for i in range(2,n+1):
    ans.append([1,i])
  a=m-k
  for i in range(2,n+1):
    for j in range(i+1,n+1):
      if a>0:
        a-=1
        ans.append([i,j])
      else:
        continue

print(len(ans))
for i , j in ans:
  print(i,j)
