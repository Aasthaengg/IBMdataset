
from bisect import bisect_left

N = int(input())
X = list(map(int, input().split()))

X.sort()
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        k = bisect_left(X, X[i] + X[j])
        ans += k - j - 1

print(ans)
