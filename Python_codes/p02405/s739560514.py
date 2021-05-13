import sys

while True:
    h, w = map(int, sys.stdin.readline().split(' '))
    if h == 0 and w == 0:
        break

    for i in range(h):
        for j in range(w):
            sys.stdout.write('#' if (i+j) % 2 == 0 else '.')
        print ''
    print ''