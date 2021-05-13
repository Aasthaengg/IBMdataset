import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a = int(input())
b = int(input())
c = int(input())
x = int(input())
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500 + j*100 + k*50 == x:
                ans += 1
print(ans)