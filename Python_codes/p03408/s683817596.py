import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
blue = []
red = []
for i in range(n):
    s = input()
    blue.append(s)
m = int(input())
for i in range(m):
    t = input()
    red.append(t)
for i in range(n):
    c = blue[i]
    chk = blue.count(c) - red.count(c)
    if chk > ans:
        ans = chk
print(ans)