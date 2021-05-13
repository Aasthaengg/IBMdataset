m,n=map(int,input().split())
a =[]
for _ in range(m):
    a.append(list(map(int,input().split())))
for index in range(m):
    a[index].append(sum(a[index]))
for a_column in a:
    for num in a_column[:-1]:
        print(num, end=' ')
    print(a_column[-1])
for row_index in range(n):
    sum = 0
    for a_column in a:
        sum += a_column[row_index]
    print(sum, end=' ')
sum = 0
for a_column in a:
    sum += a_column[-1]
print(sum)

