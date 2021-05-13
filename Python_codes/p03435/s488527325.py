c = [[int(i) for i in input().split()] for j in range(3)]
f = True
a, b = c[0][0] - c[0][1], c[0][1] - c[0][2]
for i in range(1, 3):
    if not(c[i][0] - c[i][1] == a and c[i][1] - c[i][2] == b):
        f = False
a, b = c[0][0] - c[1][0], c[1][0] - c[2][0]
for i in range(1, 3):
    if not(c[0][i] - c[1][i] == a and c[1][i] - c[2][i] == b):
        f = False
print("Yes" if f else "No")