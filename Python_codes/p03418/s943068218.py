n, k = map(int, input().split())
ans = 0
for b in range(1, n+1):
    if b <= k:
        continue
    ans += int(n//b) * (b-k) + max(0, n%b-k+1)

if k == 0:
    ans = n**2

print(ans) 