m,n=map(int,input().split())
a =[]
for _ in range(m):
    a.append(list(map(int,input().split())))
for index in range(m):
    a[index].append(sum(a[index]))
for a_column in a:
    print(' '.join(map(str, a_column)))
a.append([0]*(n+1))
for row_index in range(n+1):
    for a_column in a[:-1]:
        a[-1][row_index] += a_column[row_index]
print(' '.join(map(str, a[-1])))

