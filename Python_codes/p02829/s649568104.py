a, b = [int(input()) for _ in range(2)]

ans = sum([(i + 1) for i in range(3)])
ans -= a + b

print(ans)
