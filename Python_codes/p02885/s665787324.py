a, b = map(int, input().split())

ans = a - min(a, 2 * b)
print(ans)
