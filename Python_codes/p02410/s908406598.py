n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
column = [int(input()) for _ in range(m)]
for i in range(n):
    print(sum(a * b for a, b in zip(matrix[i], column)))