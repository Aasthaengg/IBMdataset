r, c = [int(x) for x in input().split()]

matrix = []
for i in range(r):
    matrix.append([int(x) for x in input().split()])
    
for i in range(r):
    for j in range(c):
        print(matrix[i][j], '', end='')
    print(sum(matrix[i]))

crsum = 0
for j in range(c):
    csum = 0
    for i in range(r):
        csum += matrix[i][j]
    print(csum, '', end='')
    crsum += csum
print(crsum)