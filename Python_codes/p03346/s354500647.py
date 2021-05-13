import sys
from collections import Counter
N = int(input())
counter = Counter()
for n in map(int, sys.stdin):
    counter[n] = counter[n-1]+1

print(N-max(counter.values()))
