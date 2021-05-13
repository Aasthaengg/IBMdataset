import sys

data = sys.stdin.readline().strip()
a, b, c = data.split(' ')
a = int(a)
b = int(b)
c = int(c)

if a < b and b < c:
    print('Yes')
else:
    print('No')