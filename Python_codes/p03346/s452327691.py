import sys

N = int(sys.stdin.readline())
P = {int(sys.stdin.readline()): i for i in range(N)}
Q = [P[i] for i in range(1, N + 1)]

ans = 0
prv_q = 0
now = 0
for i in range(N):
    if prv_q > Q[i]:
        now = 0
    now += 1
    prv_q = Q[i]
    ans = max(ans, now)
print(N - ans)
