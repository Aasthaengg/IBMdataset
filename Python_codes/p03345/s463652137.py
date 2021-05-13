a, b, c, k = map(int, input().split())

ans = b - a if k % 2 == 1 else a - b

print(ans if ans <= 10**18 else "Unfair")
