import sys
n = int(input())
d = set()
for i in sys.stdin:
    c, s = i.split()
    if c == 'insert':
        d.add(s)
    else:
        print('yes' if s in d else 'no')
