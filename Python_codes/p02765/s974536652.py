n, r = map(int, input().split())

ans = r + (10 - min(n, 10)) * 100

print(ans)
