import bisect
from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
a = 0
Asum = list(accumulate(A))
x = bisect.bisect_right(Asum, Asum[N-1]/2)
total = Asum[N-1]
if x >= N:
    a = Asum[x-1]
    b = total-Asum[x-1]
    ans = abs(a-b)
if x == 0:
    a = Asum[x]
    b = total-Asum[x]
    ans = abs(a-b)
else:
    a = Asum[x-1]
    b = total-Asum[x-1]
    ans = abs(a-b)
    a = Asum[x]
    b = total-Asum[x]
    ans = min(ans, abs(a-b))
print(ans)
