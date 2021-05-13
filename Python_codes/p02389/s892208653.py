import sys
 
(a, b) = [int(i) for i in sys.stdin.readline().split()]
print("%d %d" % (a * b, (a + b) * 2))