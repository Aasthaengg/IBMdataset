import sys
import numpy as np

n = int(input())
b = np.array(list(map(int, input().split())))

ans = []
for i in range(n, 0, -1):
    cp = np.arange(1, i + 1)
    diff = b - cp
    if np.where(diff == 0)[0].shape[0] == 0:
        print(-1)
        sys.exit()
    else:
        rem = (np.where(diff == 0)[0]).max()
        ans.append(b[rem])
        b = np.delete(b, rem, axis=0)

print(*ans[::-1], sep="\n")