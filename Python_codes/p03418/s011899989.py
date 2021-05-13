n,k = map(int, input().split())
ans = 0
for b in range(1, n+1):
    ans += (n // b) * max(0, b-k)
    if n % b > 0:
        if k == 0:
            ans += max(0, (n % b) - k)
        else:
            ans += max(0, (n%b) - k + 1)
print(ans)