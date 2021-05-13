import math
import time
from collections import defaultdict, deque
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
n,d=map(int,stdin.readline().split())
print(math.ceil(n/(d+d+1)))