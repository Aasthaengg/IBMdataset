from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n = ii()
p = li()

min_p = p[0]
cnt = 0
for i in range(n):
    if min_p >= p[i]:
        cnt += 1
    min_p = min(min_p,p[i])
print(cnt)