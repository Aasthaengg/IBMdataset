N=int(input())
A,B=map(int,input().split())
plist=list(map(int,input().split()))

#plist.sort()
alist=[]
blist=[]
clist=[]
for p in plist:
  if p<=A:
    alist.append(p)
  elif p<=B:
    blist.append(p)
  else:
    clist.append(p)
    
print(min(len(alist),len(blist),len(clist)))