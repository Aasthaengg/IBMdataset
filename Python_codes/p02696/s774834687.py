a, b, n = map(int, input().split())
ans = (a * min(b-1, n)) // b - a * (min(b-1, n) // b)
print(ans)