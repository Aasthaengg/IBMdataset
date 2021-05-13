A = list()
b = list()

n, m = map(int, input().split(" "))

for i in range(n):
    A.append(list())
    A[i] = [int(x) for x in input().split(" ")]

for i in range(m):
    b.append(list())
    b[i] = int(input())

for i in range(n):
    c = 0
    for j in range(m):
        c += A[i][j] * b[j]
    print(c)