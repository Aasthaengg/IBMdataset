import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a = int(input())
b = int(input())
if a>b:
    print("GREATER")
elif a == b:
    print("EQUAL")
else:print("LESS")

