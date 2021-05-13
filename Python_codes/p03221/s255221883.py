n, m = map(int, input().split())

arr = [[] for _ in range(n)] 

p = [0] * m
y = [0] * m

for i in range(m):
    p[i], y[i] = map(int, input().split())
    arr[p[i]-1].append(y[i])    

for i in range(n):
    arr[i].sort()

import bisect
for i in range(m):
    num = bisect.bisect_left(arr[p[i]-1], y[i]) + 1
    a = str(p[i])
    b = str(num)
    print(a.zfill(6) + b.zfill(6))
