#!/usr/bin/env python

w, h, n = map(int, input().split())
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
a = [0 for _ in range(n)]
for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())

masu = [['W' for _ in range(w)] for _ in range(h)]

for i in range(n):
    if 1 == a[i]:
        for j in range(h):
            for k in range(x[i]):
                masu[j][k] = 'B' 
    if 2 == a[i]:
        for j in range(h):
            for k in range(x[i], w): 
                masu[j][k] = 'B' 
    if 3 == a[i]:
        for k in range(y[i]):
            masu[k] = ['B' for _ in range(w)]
    if 4 == a[i]:
        for k in range(y[i], h): 
            masu[k] = ['B' for _ in range(w)]

ans = 0 
for i in range(len(masu)):
    ans += masu[i].count('W')
    # print(masu[i])

print(ans)
