N=int(input())
A=list(map(int,input().split()))
A.sort()
M=N
for k in range(N-1):
    if A[k]==A[k+1] and A[k]!=0:
        for j in range(M-1,k+1,-1):
            if A[j]==A[j-1] and A[j]!=0:
                A[j]=0
                A[k]=0
                M=j
                break
count=0
dcount=0
for k in range(len(A)):
    if A[k]!=0:
        count+=1
for k in range(len(A)-1):
    if A[k]==A[k+1] and A[k]!=0:
        dcount+=2
print(count-dcount)