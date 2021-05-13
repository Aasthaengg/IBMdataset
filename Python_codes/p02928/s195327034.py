import math
N,K=map(int,input().split())
A=list(map(int,input().split()))

sumA=0
for i in range(N):
    for j in range(N):
        if A[i]>A[j] and i>j:
            sumA+=(K-1)*K//2
        if A[i]>A[j] and i<j:
            sumA+=K*(K+1)//2
    sumA=sumA % (10**9+7)
print(sumA)
