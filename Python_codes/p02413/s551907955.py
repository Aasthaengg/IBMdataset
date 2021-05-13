in_line = raw_input().split()
r = int(in_line[0])
c = int(in_line[1])
data = []
for i in range(0,r):
    in_line = raw_input().split()
    data.append([])
    for j in range(0,c):
        data[i].append(int(in_line[j]))
for data_r in data:
    sum_r = 0
    for data_c in data_r:
        sum_r += data_c
        print data_c,
    data_r.append(sum_r)
    print sum_r
for j in range(0,c+1):
    sum_c = 0
    for i in range(0,r):
        sum_c += data[i][j]
    print sum_c,