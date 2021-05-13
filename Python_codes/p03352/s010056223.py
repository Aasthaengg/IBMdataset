import itertools
import sys
input = sys.stdin.readline

X = int(input())
ans = 1

for b in range(2, X+1):
    for i in itertools.count(2):
        bp = b ** i
        # print(bp)
        if bp <= X:
            ans = max(ans, bp)
        else:
            break

print(ans)
