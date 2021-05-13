S = input()
r = True
if not 'KIH' in S:
    r = False
else:
    ps = ''
    for s in S:
        if s != 'A':
            ps += s
    if ps != 'KIHBR':
        r = False
    else:
        hi = S.index('H')
        bi = S.index('B')
        ri = S.index('R')
        if ri - bi > 2:
            r = False
        elif bi-hi > 2:
            r = False
        else:
            if ri < len(S)-2:
                r = False
            else:
                if S[0:2] == 'AA':
                    r = False
print('YES' if r else 'NO')


