# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = map(int, readline().split())
*a, = map(int, readline().split())
*b, = map(int, readline().split())
*c, = map(int, readline().split())

a.sort()
c.sort()

from bisect import bisect_left, bisect_right

ans = 0
for bi in b:
    ans += bisect_left(a,bi) * (n-bisect_right(c,bi))

print(ans)



