in_line = raw_input().split()
n = int(in_line[0])
m = int(in_line[1])
l = int(in_line[2])
a = []
b = []
for i in range(0,n):
    in_line = raw_input().split()
    a.append([])
    for j in range(0,m):
        a[i].append(int(in_line[j]))
for i in range(0,m):
    in_line = raw_input().split()
    b.append([])
    for j in range(0,l):
        b[i].append(int(in_line[j]))
for i in range(0,n):
    for j in range(0,l):
        col = 0
        for k in range(0,m):
            col += a[i][k]*b[k][j]
        if j == l-1:
            print col
        else:
            print col,