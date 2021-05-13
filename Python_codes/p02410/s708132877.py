n, m = [int(i) for i in input().split()]

A = []
b = []

for i in range(n):
    x = [int(j) for j in input().split()]
    A.append(x)

for i in range(m):
    b.append(int(input()))

c = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum += (A[i][j] * b[j])
    c.append(sum)

for i in range(n):
    print(c[i])