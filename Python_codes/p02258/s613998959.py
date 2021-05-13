n = input()
R = [input() for i in xrange(n)]

Rmin = n
maxdif = R[1] - R[0]

while Rmin > 0:
    tRmin = R.index(min(R[0:Rmin]))
    Rmax = R.index(max(R[tRmin:Rmin]))
    if tRmin == Rmax:
        if tRmin == n-1:
            tRmin-=1
        elif tRmin < n-1:
            Rmax = tRmin + 1
    Rmin = tRmin
    if (R[Rmax] - R[Rmin]) > maxdif:
        maxdif = R[Rmax] - R[Rmin]

print maxdif