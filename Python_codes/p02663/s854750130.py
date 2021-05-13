h1, m1, h2, m2, t = (int(x) for x in input().split())
s1 = h1 * 60 + m1
s2 = h2 * 60 + m2
ans = s2 - s1 - t
print(ans)