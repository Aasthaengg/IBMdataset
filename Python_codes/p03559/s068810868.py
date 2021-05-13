# ABC084C - Snuke Festival
# Binary search
from bisect import bisect_left, bisect_right

n = int(input())
A, B, C = [sorted(list(map(int, input().rstrip().split()))) for _ in range(3)]
lgth = len(C)
ans = 0
for i in B:
    ans += bisect_left(A, i) * (lgth - bisect_right(C, i))
print(ans)