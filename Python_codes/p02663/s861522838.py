h, m, h2, m2, k = map(int, input().split())

g = h2 * 60 + m2
s = h * 60 + m

ans = g - k - s
print(ans)