import sys
alpha = (chr(i) for i in range(97, 97+26))
l = []
for line in sys.stdin:
    l += line.lower()
count = {a:l.count(a) for a in alpha}
for k in sorted(count):
    print('%c : %i' % (k, count[k]))