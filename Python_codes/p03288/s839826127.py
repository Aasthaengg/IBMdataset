#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(readline().split()[0])
if n < 1200: print("ABC")
elif n < 2800: print("ARC")
else: print("AGC")