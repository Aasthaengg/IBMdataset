A,B,C,D = map(int, input().split())

A_B = (A+B)
C_D = (C+D)

if A_B == C_D:
    print("Balanced")
elif A_B < C_D:
    print("Right")
else:
    print("Left")