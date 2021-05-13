n, k = list(map(int, input().split()))
H = [int(input()) for _ in range(n)]
H = sorted(H)
ans = float('inf')
for i in range(n - k + 1):
    ans = min(ans, H[i + k - 1] - H[i])
print(ans)