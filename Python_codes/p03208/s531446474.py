n, k = map(int, input().split())
H = sorted([int(input()) for _ in range(n)])
ans = 10e10
for i in range(n - k + 1):
    ans = min(ans, H[i + k - 1] - H[i])

print(ans)