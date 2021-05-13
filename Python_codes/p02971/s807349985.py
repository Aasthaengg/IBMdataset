# C - Exception Handling
N = int(input())
A = [int(input()) for i in range(N)]
m1 = max(A)
i = 0
while A[i]<m1:
    i += 1
m2 = max(A[:i]+A[i+1:])
for j in range(N):
    print(m1 if i!=j else m2)