a, b, n = map(int, input().split())

t = min(b - 1, n)
ans = a * t // b - a * (t // b)

print(ans)
