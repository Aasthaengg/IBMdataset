import math
N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(N):
    if i < N - 1 and x >= a[i] or i == N - 1 and x == a[i]:
        ans += 1
        x -= a[i]
print(ans)
