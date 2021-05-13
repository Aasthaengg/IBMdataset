a, b, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
for i in range(m):
    x, y, z = map(int, input().split())
    C.append(A[x - 1] + B[y - 1] - z)

min_ = min(min(C), min(A) + min(B))
print(min_)