# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:34:09 2020

@author: ito
"""


# -*- coding: utf-8 -*-

k, s = map(int, input().split())

ans = 0

for x in range(k+1):
    for y in range(k+1):
        
        sat_z = s - x - y
        
        if sat_z >= 0 and sat_z <= k:
            ans += 1
            
print(ans)