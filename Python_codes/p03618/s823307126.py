import sys
readline = sys.stdin.readline

A = readline().rstrip()

from collections import Counter
counter = Counter(A)

ans = 1 + (len(A) * (len(A) - 1)) // 2

for val in counter.values():
  ans -= (val * (val - 1)) // 2
  
print(ans)