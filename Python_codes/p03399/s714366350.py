#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a,b)+min(c,d))