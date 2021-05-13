from bisect import bisect_right
from itertools import accumulate


N = int(input())
A = sorted(map(int, input().split()))
acc_A = list(accumulate(A))
ans = 0
for i in range(N):
    prev = i
    while True:
        idx = bisect_right(A, 2 * acc_A[prev], lo=prev) - 1
        if idx == N - 1:
            ans += 1
            break
        if idx == prev:
            break
        prev = idx
print(ans)
