import sys
import numpy as np

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n = ni()
V = np.array(nl())
C = np.array(nl())
T = V - C
ans = 0
for t in T:
    if t > 0:
        ans += t
print(ans)
