s = list(input())
A = int(s[0])
B = int(s[1])
C = int(s[2])
D = int(s[3])
if A + B + C + D == 7:
    print(str(A) + "+" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
elif A + B + C - D == 7:
    print(str(A) + "+" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
elif A + B - C + D == 7:
    print(str(A) + "+" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
elif A + B - C - D == 7:
    print(str(A) + "+" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
elif A - B + C + D == 7:
    print(str(A) + "-" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
elif A - B + C - D == 7:
    print(str(A) + "-" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
elif A - B - C + D == 7:
    print(str(A) + "-" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
elif A - B - C - D == 7:
    print(str(A) + "-" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
