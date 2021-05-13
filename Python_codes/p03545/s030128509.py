from itertools import product
s = input()
A, B, C, D = int(s[0]), int(s[1]), int(s[2]), int(s[3])

P = product([1, -1], repeat=3)

def convert(integer):
    if integer == 1:
        return "+"
    elif integer == -1:
        return "-"

for o1, o2, o3 in P:
    if A + B * o1 + C * o2 + D * o3 == 7:
        print(str(A) + convert(o1) + str(B) + convert(o2) + str(C) + convert(o3) + str(D) + "=7")
        exit()