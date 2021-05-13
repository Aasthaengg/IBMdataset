h,w=map(int,input().split())
a=[]
for i in range(h):
  a.append(list(map(int,input().split())))


xylis=[]

for i in range(h-1):
  for j in range(w-1):
    if a[i][j]%2==1:
      a[i][j]-=1
      a[i][j+1]+=1
      xylis.append([i,j,i,j+1])
  if a[i][w-1]%2==1:
    a[i][w-1]-=1
    a[i+1][w-1]+=1
    xylis.append([i,w-1,i+1,w-1])
for j in range(w-1):
  if a[h-1][j]%2==1:
    a[h-1][j]-=1
    a[h-1][j+1]+=1
    xylis.append([h-1,j,h-1,j+1])

print(len(xylis))
for xylisi in xylis:
  print(*list(map(lambda x:x+1,xylisi)))
