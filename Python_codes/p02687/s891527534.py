#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

sys.setrecursionlimit(10000)

S = input()
print('ARC' if S == 'ABC' else 'ABC')
