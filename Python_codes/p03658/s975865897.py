import sys
n,k = map(int, sys.stdin.readline().rstrip("\n").split())
l = [int(s) for s in sys.stdin.readline().rstrip("\n").split()]
l.sort(reverse=True)
print(sum(l[:k]))