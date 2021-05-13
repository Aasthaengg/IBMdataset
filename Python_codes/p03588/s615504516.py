N = int(input())
A, B = [], []
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)

max_val = max(A)
print(max_val + B[A.index(max_val)])