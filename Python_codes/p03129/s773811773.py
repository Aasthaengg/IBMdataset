n, k = map(int, input().split())

q, r = divmod(n, 2)
if k <= q + r:
    ans = "YES"
else:
    ans = "NO"

print(ans)
