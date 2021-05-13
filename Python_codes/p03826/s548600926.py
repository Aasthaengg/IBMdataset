A,B,C,D = map(int, input().split())

A_B = (A*B)
C_D = (C*D)

if A_B < C_D:
    print(C_D)
elif A_B > C_D:
    print(A_B)
else:
    print(A_B)