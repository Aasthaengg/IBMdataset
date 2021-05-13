import sys
from collections import defaultdict

N = int(input())
D = list(map(int, sys.stdin.readline().rsplit()))
M = int(input())
T = list(map(int, sys.stdin.readline().rsplit()))
q = defaultdict(int)

for d in D:
    q[d] += 1

for t in T:
    if q[t] > 0:
        q[t] -= 1
    else:
        print("NO")
        exit()

print("YES")
