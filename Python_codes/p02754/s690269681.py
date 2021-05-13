n, a, b = map(int, input().split())

d, m = divmod(n, a + b)

ans = d * a + min(m, a)

print(ans)