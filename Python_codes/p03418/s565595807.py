n, k = map(int, input().split())
if k == 0:
    print(n**2)
    exit()

ans = 0
# 割る値bを固定して該当するaの個数を足し上げる
for b in range(k+1, n + 1):
    q = n // b
    r = n % b
    if r < k:
        ans += q * (b-k)
    else:
        ans += q * (b-k) + (r-k+1)
print(ans)
