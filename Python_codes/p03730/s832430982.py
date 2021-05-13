import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a, b, c = map(int, input().split())
for i in range(1, 100000):
    if (b*i + c)%a == 0:
        print("YES")
        exit()
print("NO")