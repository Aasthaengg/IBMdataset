n,m = map(int, input().split())

# init
A = []
b = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(m):
    b.append(int(input()))


for row in range(n):
    p = 0
    for i, j in zip(A[row], b):
        p += i * j
    print(p)