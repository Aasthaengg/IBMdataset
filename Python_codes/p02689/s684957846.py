from sys import stdin
import sys, math

n,m = [int(x) for x in stdin.readline().rstrip().split()]
h = [int(x) for x in stdin.readline().rstrip().split()]

c = [1 for x in range(n)]
for i in range(m):
    a,b = [int(x) for x in stdin.readline().rstrip().split()]

    if h[a-1] >= h[b-1]: c[b - 1] = 0
    if h[a-1] <= h[b-1]: c[a - 1] = 0

print(sum(c))



