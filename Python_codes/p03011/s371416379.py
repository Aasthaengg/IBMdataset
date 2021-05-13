import sys
import itertools
rl = lambda: list(map(int, sys.stdin.readline().split()))
print(min(list(map(sum, itertools.combinations(rl(), 2)))))