n = int(input())

M = [[1] * n for i in range(n)]

if n % 2 == 0:
    for i in range(n):
        for j in range(i+1, n):
            if i + j == n-1:
                M[i][j] = 0
else:
    for i in range(n-1):
        for j in range(i+1, n-1):
            if i + j == n-2:
                M[i][j] = 0

A = []
for i in range(n):
    for j in range(i+1, n):
        if M[i][j] == 1:
            A.append([i, j])

print(len(A))
for i in range(len(A)):
    print(A[i][0]+1, A[i][1]+1)