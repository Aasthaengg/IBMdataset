H,W=map(int,input().split())
a=[list(map(int,input().split()))for i in range(H)]
l=[]
for i in range(H):
  for j in range(W):
    if a[i][j]%2:
      if i+1<H:
        a[i][j]-=1
        a[i+1][j]+=1
        l.append((i+1,j+1,i+2,j+1))
      elif j+1<W:
        a[i][j]-=1
        a[i][j+1]+=1
        l.append((i+1,j+1,i+1,j+2))
print(len(l))
for i in l:
  print(*i)