import sys
import numpy as np
input = sys.stdin.readline


n, c = map(int, input().split())
tv_guide = np.zeros((c, 10**5+1), dtype=np.int)

for _ in range(n):
    s, t, c = map(lambda x: int(x)-1, input().split())
    tv_guide[c][s:t+1] = 1

ans = 0
for time in range(10**5+1):
    count = sum(tv_guide[:,time])
    ans = max(count, ans)

print(ans)