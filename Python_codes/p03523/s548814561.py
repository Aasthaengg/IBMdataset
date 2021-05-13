x = 'KIHBR'
T = []
for i in range(1<<6):
    t = ''
    for j in range(6):
        if i&(1<<j) and j != 1 and j != 2:
            t += 'A'
        if j != 5:
            t += x[j]
    T.append(t)
S = input()
if S in T:
    print('YES')
else:
    print('NO')
