#! python3
#  solve_120_B.py

import math

A,B,K = map(int,input().split())

gcd_of_AB = math.gcd(A,B)
l = []

for i in range(1,gcd_of_AB+1):
    if gcd_of_AB % i == 0:
        l.append(i)

print(l[len(l)-K])