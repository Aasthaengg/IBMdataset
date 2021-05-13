a, b, c, k = map(int, input().split())
ans = 0
if a >= k:
    ans = k
    k = 0
else:
    k -= a
    ans = a
k -= b
if k > 0:
    ans -= k
print(ans)
