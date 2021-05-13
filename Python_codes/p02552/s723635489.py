#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

N = int(input())
res = 1-N
print(res)
