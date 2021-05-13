import sys

N, C, K = map(int, sys.stdin.readline().strip().split())
T = []
for _ in range(N):
    T.append(int(sys.stdin.readline().strip()))

T.sort()
ans = 0
n = 0
left_min = float("inf")
for t_i in T:
    left_min = min(t_i, left_min)
    if left_min + K < t_i:
        ans += 1
        left_min = t_i
        n = 1
        continue

    n += 1
    if n == C:
        ans += 1
        n = 0
        left_min = float("inf")

if n > 0:
    ans += 1

print(ans)