import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7

count_inner = 0
for i in range(N):
    for j in range(i,N):
        if A[i] > A[j]:
            count_inner += 1
count_outer = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            count_outer += 1
def fact(n):
    if n>1:
        return n*fact(n-1)%mod
    else:
        return 1

answer = (count_inner*K + count_outer*K*(K-1)//2)%mod

print(answer)