#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,k = map(int,input().split())
print(0 if n%k == 0 else 1)