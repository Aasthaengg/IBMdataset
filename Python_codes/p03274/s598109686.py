n, k = map(int, input().split())
X = list(map(int, input().split()))
ans = 3 * 10 ** 8
for i in range(n - k + 1):
    left = X[i]
    right = X[i + k - 1]
    if left < 0 and right > 0:
        time = right - left + min(abs(left), abs(right))
    else:
        time = max(abs(right), abs(left))
    ans = min(ans, time)
print(ans)