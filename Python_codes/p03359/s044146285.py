#!/usr/bin/env python3
import numpy as np
import math
import re

n = input()
n = re.split(" ",n)
a = int(n[0])
b = int(n[1])
if( b < a ):
    print(a-1)
else:
    print(a)