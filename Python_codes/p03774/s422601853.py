n, m = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(m):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

for i in range(n):
    dis = []
    for j in range(m):
        dis.append(abs(A[i] - C[j]) + abs(B[i] - D[j]))
    mi = min(dis)
    for j in range(m):
        if dis[j] == mi:
            print(j + 1)
            break
