n, m = map(int, input().split())

ans = 0
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        div = m // i

        if i <= m // n:
            ans = max(ans, i)

        if div <= m // n:
            ans = max(ans, div)

print(ans)
