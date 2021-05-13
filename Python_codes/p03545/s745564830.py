ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
for i in range(1):
    if A + B + C + D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
        exit()
    if A - B + C + D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
        exit()
    if A + B - C + D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
        exit()
    if A + B + C - D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
        exit()
    if A - B - C + D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
        exit()
    if A - B + C - D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
        exit()
    if A + B - C - D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
        exit()
    if A - B - C - D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
        exit()