n=int(input())
alist=[]
blist=[]
for i in range(n):
  x,y=map(int, input().split())
  alist.append(x+y)
  blist.append(x-y)
print(max(max(alist)-min(alist),max(blist)-min(blist)))