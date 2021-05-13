a, b, c, k = (int(x) for x in input().split())
ans = 0

if k < a: ans += k * 1
elif a <= k <= a + b: ans += a * 1
elif a + b < k <= a + b + c: ans += a * 1 + (k - (a + b)) * (-1)
print(ans)