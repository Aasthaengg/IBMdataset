import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

if sorted(s) < sorted(t, reverse=True):
    print("Yes")
else:
    print("No")