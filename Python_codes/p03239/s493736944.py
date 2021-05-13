import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n, T = map(int, input().split())
cost = False
for i in range(n):
    c, t = map(int, input().split())
    if t > T:
        pass
    else:
        if cost == False:
            cost = c
        else:
            if cost > c:
                cost = c
if cost == False:
    print("TLE")
else:
    print(cost)