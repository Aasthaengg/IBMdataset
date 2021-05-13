import sys

n = int(input())
dct = set()

for line in sys.stdin:

    cmd, val = line.strip().split()

    if cmd == 'insert':
        dct.add(val)

    else:
        if val in dct:
            print('yes')
        else:
            print('no')

