# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:27:43 2020

@author: NEC-PCuser
"""

N = int(input())

ans = 0
a_count = 0
b_count = 0
ab_count = 0
for i in range(N):
    s = input()
    if (s[0] == "B" and s[len(s) - 1] == "A"):
        ab_count += 1
    else:
        if (s[0] == "B"):
            b_count += 1
        if (s[len(s) - 1] == "A"):
            a_count += 1
    
    ans += s.count("AB")
    
    
plus = min([a_count, b_count])
    
if (ab_count != 0 and a_count + b_count > 0):
    plus += ab_count
elif (ab_count != 0):
    plus += (ab_count - 1)

print(ans + plus)