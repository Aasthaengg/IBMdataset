import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
k = int(input())
X = list(map(int, input().split()))
for i in range(n):
    if X[i]*2 < abs(k-X[i])*2:
        ans += X[i]*2
    else:
        ans += abs(k-X[i])*2
print(ans)