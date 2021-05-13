n,m=map(int, input().split())
alist=[]
blist=[]
for i in range(m):
  a,b=map(int, input().split())
  alist.append(a)
  blist.append(b)
maxa=max(alist)
minb=min(blist)
if minb>=maxa:
  print(minb-maxa+1)
else:
  print(0)