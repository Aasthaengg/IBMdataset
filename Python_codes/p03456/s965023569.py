#!/usr/bin/env python3
import math 
a, b = input().split()
c = int(a + b)

if math.sqrt(c).is_integer():
    print("Yes")
else:
    print("No")
