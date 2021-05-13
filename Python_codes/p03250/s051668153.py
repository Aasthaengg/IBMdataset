a, b, c = map(int, input().split())

res = 0
res = max(res, a * 10 + b + c)
res = max(res, b * 10 + a + c)
res = max(res, c * 10 + b + a)

print(res)
