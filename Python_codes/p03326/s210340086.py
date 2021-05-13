#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)

    res = 0
    for pattern in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
        (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]:
        li = []
        for i in range(n):
            kariscore = pattern[0] * x[i] + pattern[1] * y[i] + pattern[2] * z[i]
            li.append((kariscore, i))
        li = list(reversed(sorted(li)))
        eatlist = [i for k, i in li[:m]]
        res = max(res, score(eatlist, x, y, z))
    print(res)

def score(eatlist, x, y, z):
    xx = 0
    yy = 0
    zz = 0
    for i in eatlist:
        xx += x[i]
        yy += y[i]
        zz += z[i]
    return abs(xx) + abs(yy) + abs(zz)

if __name__ == "__main__":
    main()
