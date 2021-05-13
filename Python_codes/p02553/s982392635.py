a,b,c,d = list(map(int, input().split()))

p = a * c
o = a * d
i = b * c
u = b * d

print(max(p, o, i, u))