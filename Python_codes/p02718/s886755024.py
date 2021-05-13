# coding: utf-8
# Your code here!

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
sum_A=sum(A)
count=0
for i in range(M):
    if A[i]/sum_A>=1/(4*M):
        count+=1

if count==M:
    print("Yes")
else:
    print("No")