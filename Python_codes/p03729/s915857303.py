line = input()
Line = line.split()
A = Line[0]
B = Line[1]
C = Line[2]

if A[-1] == B[0] and B[-1] == C[0]:
    print('YES')
else:
    print('NO')