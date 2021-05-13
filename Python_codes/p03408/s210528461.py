import collections
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
x = collections.Counter(s)
for i in t:
    x[i] -= 1
print(max(max(x.values()),0))