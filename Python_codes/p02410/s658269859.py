n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A.append(input().split())
for i in range(m):
    B.append(int(input()))

C = []
for i in range(n):
    C.append(0)
    for j in range(m):
        C[i] += int(A[i][j]) * B[j]
    print(C[i])