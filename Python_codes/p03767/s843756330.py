import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()

# print(a)
ans = 0
a = a[n:]
a.reverse()
print(sum(a[1::2]))