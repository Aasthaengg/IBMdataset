X = input()

A, B, C, D = [int(X[i]) for i in range(4)]

for i in range(2**3, 2**4):
    s = format(i, 'b')[1:]
    E = A + (-1) ** int(s[0]) * B + (-1) ** int(s[1]) * C + (-1) ** int(s[2]) * D
    if E == 7:
        break

op = ['+', '-']

print(str(A) + op[int(s[0])] + str(B) + op[int(s[1])] + str(C) + op[int(s[2])] + str(D) + '=7')