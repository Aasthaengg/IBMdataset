import math
import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
v = sys.stdin.readline().rstrip()

# s = s[:3]
# v = v[-3:]
ans = 0

for i in range(min(len(s), len(v))):
    if s[-i - 1:] == v[:i + 1]:
        ans = i + 1

print(n * 2 - ans)