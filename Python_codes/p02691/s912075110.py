from collections import Counter
import sys
input = sys.stdin.readline

n: int = int(input())
a = list(map(int, input().split()))
minus = Counter([i-a[i] for i in range(n)])
plus = Counter([i+a[i] for i in range(n)])

cnt: int = 0
i: int
for i in minus:
    if i in plus:
        cnt += minus[i] * plus[i]
print(cnt)
