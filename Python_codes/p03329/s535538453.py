def f(yen, coin, cnt=0):
    while yen > 0: cnt += yen % coin; yen //= coin
    return cnt

ans = n = int(input())
for yen6 in range(0, n+1):
    ans = min(ans, f(n-yen6, 9, f(yen6, 6)))
print(ans)
