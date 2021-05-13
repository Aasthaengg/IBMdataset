c = [list(map(int,input().split())) for _ in range(3)]
a = []
b = []
for i in range(3):
    a.append(abs(c[i][0]-c[i][1]))
    a.append(abs(c[i][1]-c[i][2]))
for i in range(3):
    b.append(abs(c[0][i]-c[1][i]))
    b.append(abs(c[1][i]-c[2][i]))
if a[0] == a[2] and a[2] == a[4] and b[0] == b[2] and b[2] == b[4] \
    and a[1] == a[3] and a[3] == a[5] and b[1] == b[3] and b[3] == b[5]:
    print('Yes')
    exit()
print('No')
