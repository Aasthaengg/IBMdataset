N=int(input())
A=list(map(int,input().split()))
flag=0
count=1
for i in range(1,N):
    if A[i-1]<A[i]:
        if flag==-1:
            count+=1
            flag=0
        elif flag==0:
            flag=1
    elif A[i-1]>A[i]:
        if flag==1:
            count+=1
            flag=0
        elif flag==0:
            flag=-1
print(count)