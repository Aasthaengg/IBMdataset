import sys
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

counter = Counter(read().rstrip()).values()

counter

N = sum(counter)
x = N * (N - 1) // 2 + 1
x -= sum(x * (x - 1) // 2 for x in counter)
print(x)