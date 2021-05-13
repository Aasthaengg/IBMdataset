import sys

a = []
for line in sys.stdin:
    a.append(str(line))
a = ''.join(a).lower()

d = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    d[i] = 0
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
        d[i] += 1
for i in "abcdefghijklmnopqrstuvwxyz":
    print i,':',d[i]