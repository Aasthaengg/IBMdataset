import sys
import numpy as np  # noqa

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())
if N % 1000 == 0:
    print(0)
else:
    print(1000 - N % 1000)
