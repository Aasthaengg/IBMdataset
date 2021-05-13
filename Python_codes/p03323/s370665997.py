#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a,b = map(int,input().split())
print("Yay!" if a <= 8 and b <= 8 else ":(")