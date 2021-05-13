n = int(input())

C = [[1 for i in range(n)] for j in range(n)]
for i in range(n):
    C[i][i] = 0
if n%2 == 0:
    for i in range(n):
        C[i][n-1-i] = 0
else:
    for i in range(n):
        C[i][n-2-i] = 0

print(n*(n-1)//2-n//2)
for i in range(n):
    for j in range(n):
        if i<j and C[i][j] == 1:
            print(i+1,j+1)