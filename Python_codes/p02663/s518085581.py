h1, m1, h2, m2, k = map(int, input().split())
t = (h2 - h1) * 60 + (m2 - m1)
ans = t - k
print(ans)