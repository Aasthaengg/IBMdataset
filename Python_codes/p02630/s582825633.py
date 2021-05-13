# -*- coding: utf-8 -*-

import sys
input = sys.stdin.buffer.readline
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

temp = [0]*(10**5+1)
ans = 0

for i in A:
    temp[i] += 1
    ans += i
for i in range(Q):
    B, C = map(int,input().split()) 
    ans += temp[B]*(C-B)
    temp[C] += temp[B]
    temp[B] = 0

    print(ans)
    
