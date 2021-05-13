import sys
import bisect
N, M = map(int, input().split())
A = sorted(map(int, input().split()))
CB = [None] * M
for i in range(M):
    b, c = map(int, sys.stdin.readline().split())
    CB[i] = (c, b)
CB.sort(reverse=True)

i = 0
ans = 0
for c, b in CB:
    x = bisect.bisect_left(A, c, i)
    count = min(x - i, b)
    ans += c * count
    i += count
for j in range(i, N):
    ans += A[j]
print(ans)