n = int(input())
A, B, C = [], [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append([a + b, i])
C = sorted(C, reverse=True)

suma, sumb = 0, 0
for i in range(n):
    if i % 2:
        sumb += B[C[i][1]]
    else:
        suma += A[C[i][1]]
print(suma - sumb)