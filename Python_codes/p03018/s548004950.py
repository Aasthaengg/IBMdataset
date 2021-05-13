S = input()
S = S.replace('BC', 'X')

ret = 0
a_frq = 0
for s in S:
    if s == 'A':
        a_frq += 1

    elif s == 'X':
        ret += a_frq

    else:
        a_frq = 0

print(ret)
