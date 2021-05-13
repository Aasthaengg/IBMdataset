import sys
n = int(sys.stdin.readline())
l = [int(i) for i in sys.stdin.readline().split()]
print(min(l), max(l), sum(l))