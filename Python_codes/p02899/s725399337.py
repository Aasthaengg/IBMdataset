import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
A=[(e,i) for i,e in enumerate(list(map(int,input().split())))]
#print(A)
A.sort(key=lambda tup: tup[0])
#print(A)
for e,i in A:
    print(i+1)