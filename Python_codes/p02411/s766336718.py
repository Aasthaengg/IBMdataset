def seiseki(m,f,r):
    if m == -1 or f == -1:
        return 'F'
    if m + f >= 80:
        return 'A'
    if m + f >= 65 and m + f < 80:
        return 'B'
    if m + f >= 50 and m + f < 65:
        return 'C'
    if m + f >= 30 and m + f < 50 and r >= 50:
        return 'C'
    if m + f >= 30 and m + f < 50:
        return 'D'
    if m + f < 30:
        return 'F'

import sys

for l in sys.stdin:
    m, f, r = map(int,l.split())
    if f == -1 and m == -1 and r == -1:
        break
    print (seiseki(m,f,r))