N,M=map(int,input().split())
alist=list(map(int,input().split()))

slist=[0]
asum=0
for a in alist:
  asum+=a
  slist.append(asum%M)
#print(alist)
#print(slist)

answer=0
sdic={}
for s in slist:
  if s in sdic:
    answer+=sdic[s]
    sdic[s]+=1
  else:
    sdic[s]=1

print(answer)