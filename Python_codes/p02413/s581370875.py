matrix=[]
r,c = map(int,input().split())

for i in range(r):
    a=list(map(int,input().split()))
    matrix.append(a)

for rows in matrix:
    rows.append(sum(rows))

column_sum = []
for j in range(c+1):
    element_sum = 0
    for k in range(r):
        element_sum += matrix[k][j]
    column_sum.append(element_sum)

for p in matrix:
    print(" ".join(map(str,p)))
    
print(" ".join(map(str,column_sum)))