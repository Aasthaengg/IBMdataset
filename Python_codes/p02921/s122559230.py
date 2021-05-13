S = input()
T = input()
L = 0
A = S[0] 
B = S[1]
C = S[2]
D = T[0]
E = T[1]
F = T[2]
if A == D:
    L += 1
if B == E:
    L += 1
if C == F:
    L += 1
print(L)