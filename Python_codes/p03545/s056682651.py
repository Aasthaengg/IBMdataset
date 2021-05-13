from itertools import product

m = input()
n = m[0] + 'x' + m[1] + 'y' + m[2] + 'z' + m[3]

for i in product([0,1], repeat=3):
    if i[0] == 0:
        l = n.replace('x', '+')
    elif i[0] == 1:
        l = n.replace('x', '-')

    if i[1] == 0:
        l = l.replace('y', '+')
    elif i[1] == 1:
        l = l.replace('y', '-')

    if i[2] == 0:
        l = l.replace('z', '+')
    elif i[2] == 1:
        l = l.replace('z', '-')

    if eval(l) == 7:
        print(l + '=7')
        exit()
