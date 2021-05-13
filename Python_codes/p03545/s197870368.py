s = list(input())
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

def p_mark(j):
    if j % 2 == 0:
        return '+'
    else:
        return '-'

for i in range(2 ** 3):
    j = i
    p = a
    x = p_mark(j)
    if x == '+':
        p += b
    else:
        p -= b
    j = j // 2
    y = p_mark(j)
    if y == '+':
        p += c
    else:
        p -= c
    j = j // 2
    z = p_mark(j)
    if z == '+':
        p += d
    else:
        p -= d
    if p == 7:
        print(str(a) + x + str(b) + y + str(c) + z + str(d) + '=7')
        break