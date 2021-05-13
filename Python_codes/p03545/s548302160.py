s = input()

for i in range(2**3):
    ss = ''
    for j in range(4):
        ss += s[j]
        if j < 3:
            if (i >> j) & 1 == 1:
                ss += '+'
            else:
                ss += '-'
    if eval(ss) == 7:
        break
print(ss+'=7')