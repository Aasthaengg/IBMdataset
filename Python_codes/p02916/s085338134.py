N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
satisfy = 0
for i in range(N):
    satisfy += B[A[i]-1]
    if i <= N-2:
        if A[i+1]-A[i] == 1:
            satisfy += C[A[i]-1]
print(satisfy)