import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

arr = np.arange(n) + 1
diff = a - arr

diff.sort()

diff = diff - np.median(diff)

print(int(np.abs(diff).sum()))