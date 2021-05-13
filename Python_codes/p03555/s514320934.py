C = [input() for _ in range(2)]
f = C[0][0] == C[1][2] and C[0][1] == C[1][1] and C[1][0] == C[0][2]
if f:
    print('YES')
else:
    print('NO')