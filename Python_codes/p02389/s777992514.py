import sys

a,b = map(int,sys.stdin.readline().split())
area = a*b
surround = 2*(a+b)
print("%d %d" % (area, surround))