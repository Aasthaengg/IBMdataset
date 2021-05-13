import bisect
from itertools import accumulate

N , M , K = map(int , input().split())
a = list(map(int , input().split()))
b = list(map(int , input().split()))
a = list(accumulate(a))
b = list(accumulate(b))
a.insert(0,0)

ans = 0
for i in range(N + 1):
    if a[i] > K:
        break
    ans = max(ans , i + bisect.bisect_right(b, K - a[i]))
print(ans)
