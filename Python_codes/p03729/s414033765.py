A, B, C = input().split()

A_e = A[-1]
B_f = B[0]
B_e = B[-1]
C_f = C[0]

if (A_e == B_f) and (B_e == C_f):
    print("YES")

else:
    print("NO")