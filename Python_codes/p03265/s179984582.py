import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main(x1, x2, y1, y2):
    a = x1 + y1 * 1j
    b = x2 + y2 * 1j
    c = b + (b-a) * 1j
    d = a + (a-b) * (-1j)
    print(int(c.real), int(c.imag), int(d.real), int(d.imag))

x1, y1, x2, y2 = map(int, readline().split())
main(x1, x2, y1, y2)
