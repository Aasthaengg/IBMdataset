import sys
import bisect
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n, m, k = inm()
a = inl()
b = [0] + inl()
count = 0
prev = 0
for i in range(n-1):
    a[i+1] += a[i]
for i in range(m+1):
    if b[i]+prev > k:
        break
    j = bisect.bisect(a, (k - b[i] - prev))
    count = max(count, i + j)
    prev += b[i]
print(count)