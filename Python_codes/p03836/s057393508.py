import sys


def input(): return sys.stdin.readline().strip()


def resolve():
    s1, s2, t1, t2 = map(int, input().split())
    l = []
    yoko = t1 - s1
    tate = t2 - s2
    if yoko > 0 and tate > 0:
        l.append('R' * yoko + 'U' * tate)
        l.append('L' * yoko + 'D' * tate)
        l.append('D' + 'R' * (yoko + 1) + 'U' * (tate + 1) + 'L')
        l.append('U' + 'L' * (yoko + 1) + 'D' * (tate + 1) + 'R')
        print(''.join(l))
    elif yoko > 0 and tate < 0:
        tate = -tate
        l.append('R' * yoko + 'D' * tate)
        l.append('L' * yoko + 'U' * tate)
        l.append('U' + 'R' * (yoko + 1) + 'D' * (tate + 1) + 'L')
        l.append('D' + 'L' * (yoko + 1) + 'U' * (tate + 1) + 'R')
        print(''.join(l))
    elif yoko < 0 and tate > 0:
        yoko = -yoko
        l.append('L' * yoko + 'U' * tate)
        l.append('R' * yoko + 'D' * tate)
        l.append('D' + 'L' * (yoko + 1) + 'U' * (tate + 1) + 'R')
        l.append('U' + 'R' * (yoko + 1) + 'D' * (tate + 1) + 'L')
        print(''.join(l))
    else:
        yoko = -yoko
        tate = -tate
        l.append('L' * yoko + 'D' * tate)
        l.append('R' * yoko + 'U' * tate)
        l.append('U' + 'L' * (yoko + 1) + 'D' * (tate + 1) + 'R')
        l.append('D' + 'R' * (yoko + 1) + 'U' * (tate + 1) + 'L')
        print(''.join(l))
resolve()