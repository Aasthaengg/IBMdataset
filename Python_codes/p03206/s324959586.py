#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__


sys.setrecursionlimit(10000)

D = int(input())

res = ' '.join(['Christmas'] + ['Eve'] * (25-D))

print(res)

