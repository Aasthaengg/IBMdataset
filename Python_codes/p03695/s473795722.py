#!/usr/bin/env python3

N = int(input())
A = [int(i) for i in input().split()]

rate = [400,800,1200,1600,2000,2400,2800,3200]
R = [False]*len(rate)
red_plus = 0

for a in A:
    if a >= rate[-1]:
        red_plus += 1
    else:
        for i,r in enumerate(rate):
            if a < r:
                R[i] = True
                break
    
if R.count(True) == 0:
    print(1, R.count(True)+red_plus)
else:
    print(R.count(True), R.count(True)+red_plus)
    

