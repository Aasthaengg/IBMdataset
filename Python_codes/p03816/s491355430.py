# coding: utf-8
# Your code here!
N=int(input())
A=list(map(int,input().split()))
A.sort()
#print(A)
C=[]
cnt=1
D=0
for i in range(N-1):
    if A[i]==A[i+1]:
        cnt+=1
    else:
        C.append(cnt-1)
        D+=cnt-1
        cnt=1
C.append(cnt-1)
D+=cnt-1
#print(C)


if D%2==0:
    print(len(C))
else:
    print(len(C)-1)