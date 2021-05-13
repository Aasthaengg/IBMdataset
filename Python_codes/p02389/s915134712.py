import sys

data = sys.stdin.readline().strip().split(' ')
a = int(data[0])
b = int(data[1])
print('%d %d' % (a * b, (a + b) * 2))