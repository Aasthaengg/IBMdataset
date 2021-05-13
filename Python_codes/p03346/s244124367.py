import sys

n = int(sys.stdin.readline())
p = [None] * n
for i in range(n):
    p[i] = int(sys.stdin.readline())
a = [None] * n
for i in range(n):
    a[p[i]-1] = i
prv = -1
mx = 1
nw = 0
for i in range(n):
    if prv < a[i]:
        nw += 1
        mx = max(mx, nw)
    else:
        nw = 1
    prv = a[i]
print(n-mx)
