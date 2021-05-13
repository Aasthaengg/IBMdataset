import numpy as np

n, m, c = map(int, input().split())
array = np.array(list(map(int,input().split())))
nm = []
for _ in range(n):
    _ = list(map(int,input().split()))
    nm.append(_)

count = 0
for _ in nm:
    if np.inner(array, _)+c>0:
        count += 1
print(count)