diagonal_string = []
for i in range(3):
    d = input()
    c = []
    for j in d:
        c.append(j)
    diagonal_string.append(c)

c11 = diagonal_string[0][0]
c22 = diagonal_string[1][1]
c33 = diagonal_string[2][2]
print("{}{}{}".format(c11,c22,c33))