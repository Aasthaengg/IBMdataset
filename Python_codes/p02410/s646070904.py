m,n = map(int,input().split())
matrix_1 = []
matrix_2 = []
matrix_new = []

for i in range(m):
    x = list(map(int,input().split()))
    matrix_1.append(x)

for j in range(n):
    y = int(input())
    matrix_2.append(y)

c=0
while c<m:
    element = 0
    for j in range(n):
        element += matrix_1[c][j]*matrix_2[j]
    matrix_new.append(element)
    c+=1

for p in range(len(matrix_new)):
    print(matrix_new[p])