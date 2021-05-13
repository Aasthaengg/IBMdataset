(n,m) = [int(i) for i in input().split()]

matrix = []
vector = []
product = [0 for d in range(n)]

for nc in range(n):
    matrix.append([int(i) for i in input().split()])

for mc in range(m):
    vector.append(int(input()))

for nc in range(n):
    for mc in range(m):
        product[nc] += matrix[nc][mc] * vector[mc]

[print(product[nc]) for nc in range(n)]