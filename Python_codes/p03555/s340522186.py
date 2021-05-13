C = list(input() for i in range(2))
A = C[0]
B = C[1][::-1]

if A == B:
    print('YES')
else:
    print('NO')