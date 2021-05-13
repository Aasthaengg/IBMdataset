#!/usr/bin/env python
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0 

for i in range(1, n+1):
    score = i 
    tmpans = 1/n 
    while score < k:
        score *= 2
        tmpans *= 1/2 
    ans += tmpans

print(ans)
