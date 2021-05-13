n,m = [int(i) for i in input().split()]

a = [[int(j) for j in input().split()] for i in range(n)]
b = [int(input()) for i in range(m)]
c = [0]*m

for i in range(n):
    for j in range(m):
        c[j] = a[i][j]*b[j]
    print(sum(c))