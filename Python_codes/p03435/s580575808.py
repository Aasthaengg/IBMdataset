c = [list(map(int, input().split())) for _ in range(3)]
# print(c)
ians = [c[0][0]-c[0][0], c[0][1]-c[0][0], c[0][2]-c[0][0]]
jans = [c[0][0]-c[0][0], c[1][0]-c[0][0], c[2][0]-c[0][0]]
# print(ians, jans)
ok = True
for i in range(1, 3):
    for j in range(3):
        # print(c[i][j]-c[i][0])
        if ians[j] != c[i][j]-c[i][0]:
            ok = False

for i in range(1, 3):
    for j in range(3):
        # print(c[j][i]-c[i][0])
        if jans[j] != c[j][i]-c[0][i]:
            ok = False

if ok:
    print('Yes')
else:
    print('No')
