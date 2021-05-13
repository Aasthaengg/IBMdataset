p, q, r = map(int, input().split())
res = p + q + r - max(p, q, r)
print(res)