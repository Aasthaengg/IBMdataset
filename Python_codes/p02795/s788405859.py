#!/usr/bin/env python3

import math
h = int(input())
w = int(input())
n = int(input())
print(math.ceil(n / h) if h > w else math.ceil(n / w))
