import numpy as np

h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

g = [[0 for _ in range(w)] for _ in range(h)]

l = []
for i in range(n):
    l.extend([i + 1] * a[i])

l = np.array(l).reshape((h,w))
cnt = 0
for i in range(h):
    if cnt % 2 == 1:
        l[i] = np.flipud(l[i])
    cnt+=1
for i in l:
    print(*i)