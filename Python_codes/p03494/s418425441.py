import math
N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    cnt = 0
    while(A[i]%2==0):
        A[i] = A[i]//2
        cnt += 1
    A[i] = cnt 

print(min(A))