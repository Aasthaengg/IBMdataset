n, k = map(int, input().split())
H = [int(input()) for _ in range(n)]
H = sorted(H, reverse=True)

ans = 10**9
for i in range(n-k+1):
    dh = H[i] - H[i+k-1]
    ans = min(ans, H[i] - H[i+k-1])
print(ans)