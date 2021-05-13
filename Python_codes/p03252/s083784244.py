s = list(input())
t = list(input())
from collections import defaultdict

def s2i(z):
    ret = []
    nz = defaultdict(int)
    for i in range(len(z)):
        if z[i] in nz:
            ret.append(nz[z[i]])
        else:
            x = len(nz) + 1
            ret.append(x)
            nz[z[i]] = x
    return ret

ss = s2i(s)
tt = s2i(t)
if ss == tt:
    print('Yes')
else:
    print('No')

