N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
pluslist=[]
minuslist=[]
cnt=0
ms=0
for i in range(N):
    if A[i]-B[i]<0:
        minuslist.append(A[i]-B[i])
    elif A[i]-B[i]>0:
        pluslist.append(A[i]-B[i])
#print(minuslist,pluslist)
ms=sum(minuslist)
cnt=cnt+len(minuslist)
pluslist.sort(reverse=True)
idx=0
#print(ms,cnt)
while (ms<0)and(idx<len(pluslist)):
    ms=ms+pluslist[idx]
    cnt=cnt+1
    idx=idx+1
if ms<0:
    print("-1")
else:
    print(cnt)