import sys
(a, b) = [int(i) for i in sys.stdin.readline().split()]
d = int(a / b)
r = a % b
f = a / b
print("%d %d %.5f" % (d, r, f))