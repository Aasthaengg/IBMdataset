n,k=map(int,input().split())
A=list(map(int,input().split()))
A=[i-1 for i in A]
seen=[-1]*n;seen[0]=0

cnt=0
now=0
roop=[0]
while 1:
    if seen[A[now]]!=-1:
        roopnum=cnt-seen[A[now]]+1
        mae=seen[A[now]]
        trueroop=roop[seen[A[now]]: cnt+1]
        #print(trueroop,roopnum,mae)
        break
    now=A[now]
    cnt+=1
    roop.append(now)
    seen[now]=cnt

if k<=mae:
    print(roop[k]+1)
else:
    print(trueroop[(k-mae)%roopnum]+1)
