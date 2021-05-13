n, m = [int(i) for i in input().split()]
A_Matrix = []
B_Matrix = []
output_list = []
tmp = 0
for i in range(n):
        A_Matrix.append([int(j) for j in input().split()])
for i in range(m):
    B_Matrix.append(int(input()))

for i in range(n):
    for j in range(m):
        tmp += A_Matrix[i][j] * B_Matrix[j]
    output_list.append(tmp)
    tmp = 0
for i in range(n):
    print(output_list[i])