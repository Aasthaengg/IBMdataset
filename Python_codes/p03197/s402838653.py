import sys
input = sys.stdin.readline
from collections import defaultdict, Counter

N = int(input())
a = [int(input()) for i in range(N)]
ans = 'first' if any([x%2 for x in a]) else 'second'
print(ans)