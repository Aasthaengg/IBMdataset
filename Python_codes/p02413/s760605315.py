r,c = map(int, input().split())
matrix = []
for i in range(r):
    a = list(map(int, input().split()))
    sum = 0
    for j in range(c):
        sum += a[j]
    a.append(sum)
    matrix.append(a)
    for k in range(c+1):
        print(a[k], end = "")
        if k != c:
            print(" ", end = "")
    print()
for l in range(c+1):
    sum2 = 0
    for m in range(r):
        sum2 += matrix[m][l]
    print(sum2, end = "")
    if l != c:
        print(" ", end = "")
print()

