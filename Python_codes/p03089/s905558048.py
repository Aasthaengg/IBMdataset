#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n=int(input())
A=list(map(int,input().split()))
used=[0]*n
ans=[]
for _ in range(n):
    for i in range(len(A)-1,-1,-1):
        if A[i]==i+1:
            ans.append(i+1); count += 1
            # print(A,i+1)
            del A[i]
            break
ans.reverse()
# print(ans)
print(*ans if count == n else [-1],sep="\n")
