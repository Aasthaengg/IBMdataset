import numpy as np

n, m = map(int, input().split())
lists = list(map(int, input().split()))

arr = np.array(lists)
days = arr.sum()

if n - days >= 0:
    print(int(n - days))
else:
    print('-1')