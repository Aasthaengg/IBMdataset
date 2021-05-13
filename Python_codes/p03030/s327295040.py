n=int(input())
alist = []
for i in range(n):
    a,b=input().split()
    alist.append([a, int(b)])
blist=sorted(alist,key=lambda x:x[1],reverse=True)
blist.sort(key=lambda x:x[0])
for i in range(n):
  print(alist.index(blist[i])+1)