h,w,d=map(int,input().split())
b=[(0--(h*w-i)//d)*[0]for i in range(d)]
a=[list(map(int,input().split()))for _ in range(h)]
for i in range(h):
  for j in range(w):
    a[i][j]-=1
    b[a[i][j]%d][a[i][j]//d]=(i,j)
bb=[[0]for _ in range(d)]
for i in range(d):
  for j in range(1,len(b[i])):
    bb[i].append(bb[i][-1]+(abs(b[i][j-1][0]-b[i][j][0])+abs(b[i][j-1][1]-b[i][j][1])))
for ll,rr in [list(map(int,input().split()))for _ in range(int(input()))]:
  l=ll-1
  r=rr-1
  print(bb[l%d][r//d]-bb[l%d][l//d])