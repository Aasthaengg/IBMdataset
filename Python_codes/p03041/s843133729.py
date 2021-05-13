import sys
rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.buffer.readline().split())
a, b = rm()
s = rr()
print(s[:b-1] + s[b-1].lower() + s[b:])
