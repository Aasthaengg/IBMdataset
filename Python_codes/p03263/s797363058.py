h,w=map(int,input().split())
a=[list(map(int,input().split()))for i in range(h)]
l=[]
for i in range(h):
 for j in range(w):
  if a[i][j]%2:
   if i+1<h:a[i][j]-=1;a[i+1][j]+=1;l.append((i+1,j+1,i+2,j+1))
   elif j+1<w:a[i][j]-=1;a[i][j+1]+=1;l.append((i+1,j+1,i+1,j+2))
print(len(l))
for i in l:print(*i)