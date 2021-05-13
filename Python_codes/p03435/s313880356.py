c = [[int(i) for i in input().split()] for j in range(3)]
b2 = c[0][1]-c[0][0]
b3 = c[0][2]-c[0][0]
a2 = c[1][0]-c[0][0]
a3 = c[2][0]-c[0][0]

d = 0
for i in range(2):
    if c[i+1][1] - c[i+1][0] == b2:
        d += 1
    if c[i+1][2] - c[i+1][0] == b3:
        d += 1
for j in range(2):
    if c[1][i+1] - c[0][i+1] == a2:
        d += 1
    if c[2][i+1] - c[0][i+1] == a3:
        d += 1
if d == 8:
    print("Yes")
else:
    print("No")
