a, b, c = map(int, input().split())

m = max([a, b, c])
ans = m * 10 + (a + b + c - m)
print(ans)
