a, b, c, d = map(int, input().split())
area1 = a * b
area2 = c * d
ans = max(area1, area2)
print(ans)