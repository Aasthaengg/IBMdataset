import sys
S = input()
A = int(S[0])
B = int(S[1])
C = int(S[2])
D = int(S[3])
hugo = [1, -1]
for b in hugo:
    AB = A+b*B
    for c in hugo:
        ABC = AB+c*C
        for d in hugo:
            ABCD = ABC+d*D
            if ABCD == 7:
                if b == 1:
                    b = "+"
                else:
                    b = "-"
                if c == 1:
                    c = "+"
                else:
                    c = "-"
                if d == 1:
                    d = "+"
                else:
                    d = "-"
                print(A, b, B, c, C, d, D, "=7", sep="")
                sys.exit()
