n = int(input())
ans = 0
if n % 2 == 0:
    denom = 2 * 5
    while denom <= n:
        ans += n // denom
        denom *= 5
print(ans)