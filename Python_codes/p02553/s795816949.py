a,b,c,d = map(int, input().split())
m1 = max(a*c, a*d)
m2 = max(b*c, b*d)
print(max(m1,m2))