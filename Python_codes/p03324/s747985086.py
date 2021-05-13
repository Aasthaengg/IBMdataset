import itertools
import sys
input = sys.stdin.readline

D, N = map(int, input().split())

n = 0
for i in itertools.count(0):
    for j in range(1, 100):
        n += 1
        if n == N:
            ans = (100 * i + j) * 100**D
            print(ans)
            break
    else:
        continue
    break
