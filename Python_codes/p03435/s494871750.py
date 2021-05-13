c = []
for i in range(3):
    c.append(list(map(int, input().split())))
jud = True
h1 = c[0][0] - c[1][0]
h2 = c[1][0] - c[2][0]
w1 = c[0][0] - c[0][1]
w2 = c[0][1] - c[0][2]
for i in range(3):
    if c[0][i] - c[1][i] != h1:
        jud = False
    if c[1][i] - c[2][i] != h2:
        jud = False
for i in range(3):
    if c[i][0] - c[i][1] != w1:
        jud = False
    if c[i][1] - c[i][2] != w2:
        jud = False
if jud:
    print("Yes")
else:
    print("No")