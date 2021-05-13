from itertools import product

N, M, *XYZ = map(int, open(0).read().split())

A = [[] for _ in range(8)]
for x, y, z in zip(*[iter(XYZ)] * 3):
    for i, (a, b, c) in enumerate(product([1, -1], repeat=3)):
        A[i].append(a * x + b * y + c * z)

B = []
for a in A:
    a.sort(reverse=True)
    B.append(sum(a[:M]))

print(max(B))