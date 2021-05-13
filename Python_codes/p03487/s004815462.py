import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

counter = Counter(A)
ans = 0
for value, count in counter.items():
    if count > value:
        ans += count - value
    elif count < value:
        ans += count

print(ans)