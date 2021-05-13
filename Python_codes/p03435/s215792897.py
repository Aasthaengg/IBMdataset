c = list(list(map(int, input().split())) for i in range(3))

d = [0, 1, 2, 0, 1]
x = c[0][0] + c[1][1] + c[2][2]
ok = True
for i in range(3):
    a = c[d[i]][0] + c[d[i+1]][1] + c[d[i+2]][2]
    b = c[d[i]][2] + c[d[i+1]][1] + c[d[i+2]][0]

    if x != a or x != b:
        ok = False

print('Yes' if ok else 'No')
