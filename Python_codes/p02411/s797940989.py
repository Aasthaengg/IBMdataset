import sys

i = 0
for line in sys.stdin:
    m,f,r = line.split()
    m,f,r = int(m),int(f),int(r)

    s = m + f
    if m == -1 and f == -1 and r == -1: break
    elif m == -1 or f == -1 or s < 30: print 'F'
    elif 30 <= s and s < 50:
        if r >= 50: print 'C'
        else: print 'D'
    elif 50 <= s and s < 65: print 'C'
    elif 65 <= s and s < 80: print 'B'
    else: print 'A'