import sys
from itertools import combinations

index = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}

N = int(sys.stdin.readline())
for _ in range(N):
    s = sys.stdin.readline().strip()
    if s[0] in index:
        index[s[0]] += 1

ans = 0
for (a, b, c) in combinations(index.items(), 3):
    ans += a[1] * b[1] * c[1]

print(ans)