import bisect
import numpy as np
n = int(input())


arr = np.arange(4500) + 1
arr = arr.cumsum()

div = bisect.bisect_left(arr, n) + 1

arr = np.arange(div) + 1
rem = arr.sum() - n
arr = arr[np.where(arr != rem)]

print(*arr, sep="\n")