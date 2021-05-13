# coding: utf-8
# Your code here!
from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = [0 for i in range(q)]
c = [0 for i in range(q)]
for i in range(q):
    bb,cc = map(int,input().split())
    b[i] = bb
    c[i] = cc

d = defaultdict(int)
sub = 0
for i in range(n):
    d[a[i]] += 1
    sub += a[i]

for i in range(q):
    if b[i] <= c[i]:
        dd = c[i]-b[i]
        sub += d[b[i]] * dd
        d[c[i]] += d[b[i]]
        d[b[i]] = 0
    else:
        dd = b[i]-c[i]
        sub -= d[b[i]] * dd
        d[c[i]] += d[b[i]]
        d[b[i]] = 0
    print(sub)
