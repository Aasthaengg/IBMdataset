import sys
input()
r = sys.stdin.readlines()
d = {}

for i in r:
    if i[0] == 'i':
        d[i[7:]] = 0
    else:
        print('yes' if i[5:] in d else 'no')