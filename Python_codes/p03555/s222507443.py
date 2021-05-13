C = [input() for _ in range(2)]
tmp = C[0] + C[1]
if tmp == tmp[::-1]:
    print('YES')
else:
    print('NO')