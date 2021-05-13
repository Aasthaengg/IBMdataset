n, k = map(int, input().split())
if k % 2 == 0:
    d = k//2
    ans = ((n // d)-(n//k)) ** 3
else:
    ans = 0
ans += (n // k) ** 3
print(ans)