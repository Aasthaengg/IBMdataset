
ABCD = str(input())
A = ABCD[0]
B = ABCD[1]
C = ABCD[2]
D = ABCD[3]

for i in range(1):
    if int(A) + int(B) + int(C) + int(D) == 7:
        print(A + "+" + B + "+" + C + "+" + D +"=7")
        break
    if int(A) - int(B) + int(C) + int(D) == 7:
        print(A + "-" + B + "+" + C + "+" + D +"=7")
        break
    if int(A) + int(B) - int(C) + int(D) == 7:
        print(A + "+" + B + "-" + C + "+" + D +"=7")
        break
    if int(A) - int(B) - int(C) + int(D) == 7:
        print(A + "-" + B + "-" + C + "+" + D +"=7")
        break
    if int(A) + int(B) + int(C) - int(D) == 7:
        print(A + "+" + B + "+" + C + "-" + D +"=7")
        break
    if int(A) - int(B) + int(C) - int(D) == 7:
        print(A + "-" + B + "+" + C + "-" + D +"=7")
        break
    if int(A) + int(B) - int(C) - int(D) == 7:
        print(A + "+" + B + "-" + C + "-" + D +"=7")
        break
    if int(A) - int(B) - int(C) - int(D) == 7:
        print(A + "-" + B + "-" + C + "-" + D +"=7")
        break
