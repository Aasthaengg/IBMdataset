ABCD = input()

for i in range(2 ** 3):
    eq = ''
    for j in range(3):
        eq += ABCD[j]
        if (i >> j) & 1:
            eq += '+'
        else:
            eq += '-'
    else:
        eq += ABCD[3]
    if eval(eq) == 7:
        print(eq + '=7')
        exit()
