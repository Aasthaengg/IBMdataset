import sys

s = sys.stdin.read().rstrip()
if len(s) % 2 == 1:
    s = s[::-1]
print(s)
