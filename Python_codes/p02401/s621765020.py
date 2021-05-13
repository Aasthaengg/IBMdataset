import sys
for line in sys.stdin:
    a,b,c = line.split()
    a,c = int(a), int(c)
    p = '+-*/?'.index(b)
    if p == 0: a += c
    elif p == 1: a -= c
    elif p == 2: a *= c 
    elif p == 3: a /= c
    elif p == 4: break
    print a