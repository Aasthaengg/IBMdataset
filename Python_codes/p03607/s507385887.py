import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
c = Counter(A)
print(sum(map(lambda x: x % 2, c.values())))