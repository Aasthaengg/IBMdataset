#!/usr/bin/env python3
import numpy as np
import math
import re

n = input()

n = re.split(" ",n)

a = int(n[0])
b = int(n[1])

x = a + b
y = a - b
z = a*b

print(max(x,y,z))