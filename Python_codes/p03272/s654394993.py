#!/usr/bin/env python3
import re

n = input()
n = re.split(" ",n)

N = int(n[0])
i = int(n[1])

if(N == i):
    print(1)
else:
    print(N - i + 1)