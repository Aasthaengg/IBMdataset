import sys
from collections import Counter

N = int(sys.stdin.readline())
D = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
T = map(int, sys.stdin.readline().split())

diffs = Counter(D)
problems = Counter(T)

for diff, count in problems.items():
    if diff not in diffs:
        break
    if diffs[diff] < count:
        break
else:
    print("YES")
    sys.exit()

print("NO")