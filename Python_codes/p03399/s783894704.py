from sys import stdin
import numpy as np
import math

li = [int(stdin.readline().rstrip()) for _ in range(4)]

print(min(li[0],li[1])+min(li[2],li[3]))