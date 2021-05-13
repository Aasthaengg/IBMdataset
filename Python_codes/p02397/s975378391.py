import sys
for line in sys.stdin:
    x, y = map(int, line.split())
    if x == y == 0:
        break
    else:
        print ' '.join(map(str, sorted([x, y])))