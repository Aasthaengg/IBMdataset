k, a, b = map(int, input().split())

if a >= b:
    ans = k + 1
    print(ans)
    exit()

if (a - 1) >= k:
    ans = k + 1
    print(ans)
    exit()

ans = 1
ans += a - 1
q, r = divmod(k - (a - 1), 2)
ans += (b - a) * q
ans += r
ans = max(ans, k + 1)

print(ans)
