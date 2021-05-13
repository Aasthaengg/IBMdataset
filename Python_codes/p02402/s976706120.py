import sys
input()
x = list(map(int,sys.stdin.readline().split()))
print("{0} {1} {2}".format(min(x),max(x),sum(x)))