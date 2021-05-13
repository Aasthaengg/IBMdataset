import sys


def input(): return sys.stdin.readline().strip()


def resolve():
    s1, s2, t1, t2 = map(int, input().split())
    l = []
    yoko = t1 - s1
    tate = t2 - s2
    a,c,f,h='R','L','L','R'
    b,d,e,g='U','D','D','U'
    l.append(a*yoko+b*tate+c*yoko+d*tate)
    l.append(e+a*(yoko+1)+b*(tate+1)+f)
    l.append(g+c*(yoko+1)+d*(tate+1)+h)
    print(''.join(l))
resolve()