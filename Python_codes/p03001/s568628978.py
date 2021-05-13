#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

W, H, x, y = map(int, input().split())

area = W*H / 2
if x*2 == W and y*2 == H:
   print('%f 1' % (area))
else:
   print('%f 0' % (area))

