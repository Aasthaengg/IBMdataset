import sys

D = {}
input()
for line in sys.stdin:
    if line[0] == "f":
        print('yes' if line[5:] in D else 'no')
    else:
        D[line[7:]] = 0

