import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
n = readline().rstrip()
a = sorted(map(int,readline().split()))
print(a[-1] - a[0])