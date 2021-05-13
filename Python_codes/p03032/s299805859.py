# -*- coding: utf-8 -*-
#D - equeue
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int, readline().split())
V = list(map(int,readline().split()))

ans = 0
for l in range(min(K,N)+1):
    for r in range(min(K,N)-l+1):
        res = K - (l+r)
        minus = [] 
        total = sum(V[:l])+sum(V[N-r:])
        for i in range(l):
            if V[i] < 0:
                minus.append(V[i])        
        for i in range(r):
            if V[-i-1] < 0:
                minus.append(V[-i-1])
        minus.sort()
        S = len(minus)
        rep = sum(minus[:min(S+1,res)])
        total -= rep
        # print(l,r,total,rep)
        ans = max(total,ans)
print(ans) 