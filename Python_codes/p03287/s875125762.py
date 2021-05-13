from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))

amount = [0] * (N+1)
for i in range(N):
    amount[i+1] = amount[i] + A[i]
    amount[i+1] %= M

ans = 0
di = defaultdict(int)
for i in range(N):
    ans += di[amount[i+1]]
    di[amount[i+1]] += 1

print(ans + di[0])

