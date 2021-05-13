a, b, c = map(int, input().split())

mi = min(min(a, b), c)
ma = max(max(a, b), c)
r = (a + b + c) - mi - ma

ans = (mi * r) * 1 if ma % 2 == 1 else 0
print(ans)
