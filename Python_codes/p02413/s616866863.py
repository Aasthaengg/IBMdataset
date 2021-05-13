N = input().split()
r = int(N[0])
c = int(N[1])
d = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    data = input().split()
    for j in range(c):
        d[i][j] = int(data[j])
sum2 = [0 for i in range(c)]
for i in range(r):
    line = ''
    for j in range(c):
        line += str(d[i][j])
        line += ' '
        sum2[j] += d[i][j]
    line += str(sum(d[i]))
    print(line)
line2 = ''
for i in range(c):
    line2 += str(sum2[i])
    line2 += ' '
print('{0}{1}'.format(line2, sum(sum2)))