n = int(input())
k = int(input())
X = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    ans += min(2 * abs(X[i - 1]), 2 * abs(X[i - 1] - k))
print(ans)