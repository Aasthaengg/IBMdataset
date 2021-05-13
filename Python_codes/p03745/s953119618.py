N=int(input())
A=list(map(int, input().split()))
if N<=2:
    print(1)
    exit()

now=0
ans=1
for i in range(1,N):
    if i==1:
        if A[i]-A[i-1]==0:
            now=0
        else:
            now=(A[i]-A[i-1])//(abs(A[i]-A[i-1]))
        if now>=1:
            plus=True
        elif now==0:
            plus=-1
        else:
            plus=False
            
    else:
        if A[i]-A[i-1]==0:
            nex=0
        else:
            nex=(A[i]-A[i-1])//(abs(A[i]-A[i-1]))
        if plus==-1:
            if nex>=1:
                plus=True
            elif nex<0:
                plus=False
        elif plus:
            if nex<0:
                plus=-1
                ans+=1
        else:
            if nex>0:
                plus=-1
                ans+=1

print(ans)

