n, m = map(int, input().split())
matrix = []
vector = []
for _ in range(n):
    matrix.append(map(int, input().split()))
for _ in range(m):
    vector.append(int(input()))
for row in matrix:
    product = 0
    for i, e in enumerate(row):
        product += e * vector[i]
    print(product)