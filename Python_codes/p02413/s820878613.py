r, c = map(int, input().split())
array = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    for j, num in enumerate(input().split()):
        array[i][j] = int(num)
for i in range(r):
    array[i][c] = sum(array[i])
for i in range(c+1):
    for j in range(r):
        array[r][i] += array[j][i]
for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(array[i][j])
        else:
            print(array[i][j], end=' ')