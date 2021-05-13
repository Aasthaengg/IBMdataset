a, b, c, d = map(int, input().split())
ac = a * c
bc = b * c
ad = a * d
bd = b * d
ans = max(ac, bc, ad, bd)
print(ans)