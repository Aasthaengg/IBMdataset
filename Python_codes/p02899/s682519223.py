import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int, input().split()))
ans = [-1]*n
for i, a in enumerate(A):
    ans[a-1] = i+1
    #print(i, a)
print(*ans)