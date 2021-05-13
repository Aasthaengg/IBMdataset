import sys

for i in sys.stdin:
    h,w = map(int,i.split())

    if h==0 and w==0:
        break

    for i in range(h):
        str = ''
        for j in range(w):
            if (i+j) % 2 == 0:
                str += '#'
            else:
                str += '.'
        print(str)
    print()