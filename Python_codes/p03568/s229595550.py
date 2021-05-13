N=int(input())
A=list(map(int, input().split()))
clist=[0]*N
loscount=0
count=1
for i in range(0,N):
    if A[i]%2==1:
        clist[i]=3
    elif A[i]%2==0:
        clist[i]=3
        loscount=loscount+1
for i in range (0,N):
    count=count*clist[i]
print(count-2**loscount)