n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
sts = 0
for i in range(n):
    sts += B[A[i] - 1]
    if 0 < i and A[i] - A[i-1] == 1:
        sts += C[A[i] - 2]
print(sts)