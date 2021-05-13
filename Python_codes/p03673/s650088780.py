from collections import deque

n = int(input())
a = list(map(int, input().split()))

res = deque()
for i in range(n):
    if i % 2 == 0:
        res.append(a[i])
    else:
        res.appendleft(a[i])

if n % 2 == 0:
    for i in range(n):
        print(res[i], end=' ')
else:
    for i in range(n-1, -1, -1):
        print(res[i], end=' ')