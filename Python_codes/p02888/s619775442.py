from bisect import bisect_left, bisect_right
from collections import Counter
N = int(input())
L = list(map(int, input().split()))
L.sort()
m = Counter(L)

ans = 0
for i, x in enumerate(L[:-2]):
    for j, y in enumerate(L[i+1:-1]):
        ans += bisect_left(L, x+y) - (i+j+2)
print(ans)