n, r = map(int, input().split())
ans = r if n > 10 else 100 * (10 - n) + r
print(ans)