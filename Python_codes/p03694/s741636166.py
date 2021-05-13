#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(input())
a = list(map(int,input().split()))
a.sort()
print(a[-1]-a[0])
