#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a,b,x = map(int,input().split())
print("YES" if a <= x <= a+b else "NO")