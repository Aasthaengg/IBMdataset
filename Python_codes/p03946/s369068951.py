# ABC047D

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))


n,t = map(int, input().split())
a = list(map(int, input().split()))

m = a[0]
best = 0
count = 0
for num in a[1:]:
    if m>num:
        m = num
    elif best<num-m:
        best = num - m
        count = 1
    elif best==num-m:
        count += 1
print(count)