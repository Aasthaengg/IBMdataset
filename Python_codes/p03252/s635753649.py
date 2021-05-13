s = input().strip()
t = input().strip()


def get_patten(l):
    pattern = []
    d = dict()
    i = ord('a')
    for c in l:
        if c not in d:
            d[c] = chr(i)
            i += 1
        pattern.append(d[c])
    return pattern


ps = get_patten(s)
pt = get_patten(t)

if ps == pt:
    print('Yes')
else:
    print('No')
