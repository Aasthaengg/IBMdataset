import sys
input = sys.stdin.readline
from collections import defaultdict, deque

x = int(input()); m = int(x ** 0.5)
while x % m: m -= 1
print(m + (x // m) - 2)