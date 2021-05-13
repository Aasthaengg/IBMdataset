def main():
    s = input()
    x, y = map(int, input().split())
    d = {}
    d[True] = []
    d[False] = []
    xf = True
    t = 0
    for i in s:
        if i == 'F':
            t += 1
        else:
            d[xf].append(t)
            xf = not xf
            t = 0
    if t > 0:
        d[xf].append(t)
    dpx = set()
    dpx.add(d[True][0])
    for i in d[True][1:]:
        dnew = set()
        for j in dpx:
            dnew.add(-i+j)
            dnew.add(i+j)
        dpx = dnew
    if x not in dpx:
        return False
    dpy = set()
    dpy.add(0)
    for i in d[False]:
        dnew = set()
        for j in dpy:
            dnew.add(-i+j)
            dnew.add(i+j)
        dpy = dnew
    if y not in dpy:
        return False
    return True
if main():
    print('Yes')
else:
    print('No')
