import sys

n = sys.stdin.readline()
list = map(int,sys.stdin.readline().split())

print('%d %d %d' % (min(list),max(list),sum(list)))