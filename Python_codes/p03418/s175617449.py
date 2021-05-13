n, k = map(int, input().split())
ans = 0
b = 3
for b in range(k+1, n+1):
    if k == 0:
        ans += n
        continue

    if n % b >= k:
        ans += n%b+1-k
    ans += n // b * (b - k)

print(ans)