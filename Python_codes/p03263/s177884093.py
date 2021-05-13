h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
ans=[]
for i in range(h-1):
  for j in range(w):
    if a[i][j]%2==1:
      a[i+1][j]+=1
      ans.append([i+1,j+1,i+2,j+1])
for i in range(w-1):
  if a[h-1][i]%2==1:
    a[h-1][i+1]+=1
    ans.append([h,i+1,h,i+2])
print(len(ans))
for m in ans:
  print(*m)
  
