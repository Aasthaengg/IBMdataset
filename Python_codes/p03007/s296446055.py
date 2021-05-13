import bisect
N = int(input())
A = sorted([int(_) for _ in input().split()])
i = bisect.bisect_left(A, 0)
if i == N:
    i -= 2
elif i:
    i -= 1
now = A[i]
ans = []
for a in A[i + 1:N - 1]:
    ans += [[now, a]]
    now -= a
ans += [[A[N - 1], now]]
now = A[N - 1] - now
for a in A[:i]:
    ans += [[now, a]]
    now -= a
print(now)
[print(*xy) for xy in ans]
