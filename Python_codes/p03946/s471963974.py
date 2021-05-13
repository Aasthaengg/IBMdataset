N,T=map(int,input().split())
alist=list(map(int,input().split()))
#print(alist)

arlist=alist[:]
for i in reversed(range(N-1)):
  arlist[i]=max(arlist[i],arlist[i+1])  
#print(arlist)

max_diff=0
for i in range(N-1):
  diff=arlist[i+1]-alist[i]
  max_diff=max(max_diff,diff)

max_diff_cnt=0
for i in range(N-1):
  diff=arlist[i+1]-alist[i]
  if diff==max_diff:
    max_diff_cnt+=1
#print(max_diff,max_diff_cnt)

print(max_diff_cnt)