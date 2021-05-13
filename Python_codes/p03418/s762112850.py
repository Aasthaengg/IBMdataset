n, k = map(int, input().split())
ans = 0
for i in range(1, n - k + 1):
    ans += ((n + 1) // (k + i)) * i + max(((n + 1) % (k + i)) - k, 0)
if k == 0:
    ans -= n
print(ans)