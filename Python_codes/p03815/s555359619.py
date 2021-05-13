# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:58:33 2020

@author: liang
"""
import math

x = int(input())

ans = x // 11 *2 + math.ceil(x%11/6)

print(ans)