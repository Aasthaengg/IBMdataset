import sys
read = sys.stdin.read
from math import gcd
from math import floor
def main():
    n, m, *a = map(int, read().split())
    if n == 1:
        r = m >= a[0]//2
        r += floor((m - a[0]//2) / a[0])
        print(int(r))
        sys.exit()
    d = [0] * n
    for i, ae in enumerate(a):
        t1 = 0
        while ae > 1:
            if ae % 2 == 0:
                t1 += 1
                ae /= 2
            else:
                break
        d[i] = t1
    d_c = [de == d[0] for de in d]
    if not all(d_c):
        print(0)
        sys.exit()
    
    div = 2
    a2 = [ae // div for ae in a]
    g = (a2[0] * a2[1]) // gcd(a2[0], a2[1])
    for i1 in range(1, n):
        g = (g * a2[i1]) // gcd(g, a2[i1])
        if g > m:
            print(0)
            sys.exit()
    r = m >= g
    r += floor((m - g) / (g * 2))
    print(int(r))

if __name__ == '__main__':
    main()