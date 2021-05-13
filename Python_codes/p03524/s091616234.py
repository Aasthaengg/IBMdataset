S = input()

A = S.count('a')
B = S.count('b')
C = S.count('c')
M = max(A, B, C)
if (A == M or A == M - 1) and (B == M or B == M - 1) and (C == M or C == M - 1):
    print('YES')
else:
    print('NO')