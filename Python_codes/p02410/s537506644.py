n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

B = []
for j in range(m):
    B.append(int(input()))

for k in range(n):
    x = 0
    for l in range(m):
        x += A[k][l] * B[l]
    print(x)