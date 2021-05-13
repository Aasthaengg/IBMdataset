a, b, c, d = map(int, input().split())
s1 = a*b
s2 = c*d
r = s1 if s1 > s2 else s2
print(r)