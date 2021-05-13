input_line = raw_input().split()
n = int(input_line[0])
m = int(input_line[1])
a = []
b = []
for i in range(0,n):
    line = raw_input().split()
    a.append([])
    for c in line:
        a[i].append(int(c))
for i in range(0,m):
    line = int(raw_input())
    b.append(line)
for i in range(0,n):
    out_sum = 0
    for j in range(0,m):
        out_sum += a[i][j]*b[j]
    print out_sum