#!/usr/bin/env python3

A, B, C = sorted([int(x) for x in input().split(" ")])

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    ans = 0
else:
    ans = A * B

print(ans)
    
    

