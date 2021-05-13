n,m = [int(x) for x in input().split()]


if n < m:
    ans = n
    m -= n*2
    if m > 0:
        ans += m // 4
else:
    ans = m // 2

print(ans)
