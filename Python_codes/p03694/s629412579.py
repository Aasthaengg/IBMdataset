import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

readline()
a = list(map(int,readline().split()))
print(max(a) - min(a))