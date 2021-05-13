# Tenka1 Programmer Beginner Contest 2017: B – Different Distribution
N = int(input())
A, B = [], []
for _ in range(N):
    tmp = input().split()
    A.append(int(tmp[0]))
    B.append(int(tmp[1]))

idx = A.index(max(A))

print(A[idx] + B[idx])