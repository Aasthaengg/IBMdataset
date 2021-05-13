s = input()
a, d = [0], [0]
for char in s[:-1]:
    if char == 'A':
        a.append(a[-1] + 1)
    else:
        a.append(a[-1])
    if char == '?':
        d.append(d[-1] + 1)
    else:
        d.append(d[-1])

c, e = [0], [0]
for char in s[::-1][:-1]:
    if char == 'C':
        c.append(c[-1] + 1)
    else:
        c.append(c[-1])
    if char == '?':
        e.append(e[-1] + 1)
    else:
        e.append(e[-1])
c = c[::-1]
e = e[::-1]

ret = 0
mod = 10 ** 9 + 7
for char, aa, dd, cc, ee in zip(s, a, d, c, e):
    if char in 'B?':
        tmp1 = aa * pow(3, dd, mod)
        if dd != 0:
            tmp1 += dd * pow(3, dd - 1, mod)

        tmp2 = cc * pow(3, ee, mod)
        if ee != 0:
            tmp2 += ee * pow(3, ee - 1, mod)

        ret += tmp1 * tmp2
        ret %= mod

print(ret)
