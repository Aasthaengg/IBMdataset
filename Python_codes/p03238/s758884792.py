#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(readline())
if n == 1:
    print("Hello World")
if n == 2:
    a = int(input())
    b = int(input())
    print(a+b)