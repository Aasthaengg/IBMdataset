import sys
import numpy as np

n = int(input())
b = np.array(list(map(int, input().split())))

ans = []
for i in range(n):
    c = np.arange(1, n - i + 1)
    diff = b - c
    if not 0 in diff:
        print(-1)
        sys.exit()
    rem = np.where(diff == 0)[0][-1]
    ans.append(rem + 1)
    b = np.delete(b, rem)

print(*ans[::-1], sep="\n")