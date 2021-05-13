# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:42:46 2020

@author: liang
"""

import math

A, B, C, D = map(int, input().split())
E = C * D // math.gcd(C,D)

B_ans = B - B//C - B//D + B//E
#print(B_ans)
A -= 1
A_ans = A - A//C - A//D + A//E
#print(A_ans)
ans = B_ans - A_ans
print(ans)