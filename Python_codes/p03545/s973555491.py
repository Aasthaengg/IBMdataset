s = input()
n = len(s)

for bit in range(1 << (n -1)):

    f = s[0]

    for i in range(n -1):
        if bit & (1 << i):
            f += '+'
        else:
            f += '-'
        f += s[i + 1]

    if eval(f) == 7:
        print(f + '=7')
        break
