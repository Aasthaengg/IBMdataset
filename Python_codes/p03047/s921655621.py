#!/usr/bin/env python3
#A
import numpy as np
import math
import re

n,k = list(map(int,re.split(" ",input())))

count = 0
for i in range(n-k+1):
    count += 1

print(count)