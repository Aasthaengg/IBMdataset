import sys
s = []
for line in sys.stdin:
    s += line.lower()
A = 'abcdefghijklmnopqrstuvwxyz'
for c in A:
    print(c+' : {}'.format(s.count(c)))