N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

m = 0
for i in range(N):
    if A[i-1] == A[i]-1 and i != 0:
        m += B[A[i]-1] + C[A[i-1]-1]
    else:
        m += B[A[i]-1]
print(m)