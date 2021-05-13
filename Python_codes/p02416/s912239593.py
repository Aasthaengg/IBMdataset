import sys

for line in sys.stdin:
    if int(line) == 0: break
    s = 0
    for c in line.strip('\n'):
        s += '0123456789'.index(c)
    print s