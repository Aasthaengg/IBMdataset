from sys import stdin, stdout
from collections import defaultdict
import math

A, B, C = map(int, stdin.readline().strip().split())

tmp = min(B + A, C)

ans = B + min(C, tmp + 1)

stdout.writelines(str(ans) + '\n')
