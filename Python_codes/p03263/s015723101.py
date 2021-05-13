h,w=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
l=[]
for i in range(h):
  if i%2==0:
    for j in range(w):
      l.append((i,j))
  else:
    for j in range(w)[::-1]:
      l.append((i,j))
ans=[]

for i in range(len(l)-1):
  if a[l[i][0]][l[i][1]]%2==1:
    ans.append([l[i][0]+1,l[i][1]+1,l[i+1][0]+1,l[i+1][1]+1])
    a[l[i][0]][l[i][1]]-=1
    a[l[i+1][0]][l[i+1][1]]+=1
print(len(ans))
for i in ans:
  print(*i)