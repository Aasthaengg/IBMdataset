def main():
    s = input()
    x, y = map(int, input().split())
    d = {}
    d[True] = {0}
    d[False] = {0}
    xf = True
    t = 0
    first = True
    for i in s:
        if i == 'F':
            t += 1
        else:
            if first:
                d[xf] = set()
                d[xf].add(t)
                first = False
            else:
                tmp = set()
                for j in d[xf]:
                    tmp.add(j-t)
                    tmp.add(j+t)
                d[xf] = tmp
            xf = not xf
            t = 0
    if t == len(s):
        d[True] = {t}
        d[False] = {0}
    elif t > 0:
        tmp = set()
        for j in d[xf]:
            tmp.add(j-t)
            tmp.add(j+t)
        d[xf] = tmp
    if x in d[True] and y in d[False]:
        return True
    return False
if main():
    print('Yes')
else:
    print('No')
