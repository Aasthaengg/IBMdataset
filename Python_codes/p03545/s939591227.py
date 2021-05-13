S = input()
A = int(S[0])
B = int(S[1])
C = int(S[2])
D = int(S[3])
if A + B + C + D == 7:
    op1 = op2 = op3 = "+"
elif A + B + C - D == 7:
    op1 = op2 = "+"
    op3 = "-"
elif A + B - C + D == 7:
    op1 = op3 = "+"
    op2 = "-"
elif A + B - C - D == 7:
    op1 = "+"
    op2 = op3 = "-"
elif A - B + C + D == 7:
    op1 = "-"
    op2 = op3 = "+"
elif A - B + C - D == 7:
    op1 = op3 = "-"
    op2 = "+"
elif A - B - C + D == 7:
    op1 = op2 = "-"
    op3 = "+"
elif A - B - C - D == 7:
    op1 = op2 = op3 = "-"
print(S[0] + op1 + S[1] + op2 + S[2] + op3 + S[3] + "=7")