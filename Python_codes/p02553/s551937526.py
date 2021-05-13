a, b, c, d = map(int, input().split())

A = a * c
B = a * d
C = b * c
D = b * d

ANS = max(A, B, C, D)

print(ANS)