import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
D = list(map(int, input().split()))
D.sort()
print(D[n//2] - D[(n//2)-1])