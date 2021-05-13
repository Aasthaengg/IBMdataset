C = [[''] * 3 for _ in range(3)]
for i in range(3):
    C[i] = list(str(input()))

print(''.join((C[0][0], C[1][1], C[2][2])))