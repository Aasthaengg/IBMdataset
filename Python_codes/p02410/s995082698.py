n, m = map(int,raw_input().split())
matrix = []
for i in range(n):
    matrix.append(map(int,raw_input().split()))
 
vector = []
for i in range(m):
    vector.append(int(raw_input()))
 
for row in range(n):
    sum = 0
    for col in range(m):
        sum += vector[col] * matrix[row][col]
    print sum