n, r = map(int, input().split())
ans = r + max(0, 100 * (10 - n))
print(ans)
