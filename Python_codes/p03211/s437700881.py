import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main(s):
    ans = 1<<10
    for i in range(len(s)-2):
        num = int(s[i:i+3])
        ans = min(abs(num-753), ans)
    return ans

s = input().strip()
print(main(s))
