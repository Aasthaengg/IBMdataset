# AGC033A

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = map(int, input().split())
s = [None] * h
for i in range(h):
    s[i] = input()

r = h
c = w
ds = [[10**15]*c for _ in range(r)]
for i in range(r):
    prev = -1
    for j in range(c):
        if s[i][j]=="#":
            prev = j
        if prev>=0:
            ds[i][j] = j-prev
    prev = -1
    for j in range(c-1,-1,-1):
        if s[i][j]=="#":
            prev = j
        if prev>=0:
            ds[i][j] = min(ds[i][j], prev-j)
for j in range(c):
    prev = -1
    prevind = -1
    for i in range(r):
        if prev<0 or ds[i][j]<prev+(i-prevind):
            prev = ds[i][j]
            prevind = i
        if prev>=0:
            ds[i][j] = min(ds[i][j], prev+(i-prevind))
    prev = -1
    prevind = -1
    for i in range(r-1, -1, -1):
        if prev<0 or ds[i][j]<prev+(prevind-i):
            prev = ds[i][j]
            prevind = i
        if prev>=0:
            ds[i][j] = min(ds[i][j], prev+(prevind-i))
print(max(max(item) for item in ds))