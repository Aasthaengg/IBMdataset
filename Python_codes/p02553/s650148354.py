a,b,c,d = map(int,input().split())
m = a*c
m = max(a*d, m)
m = max(b*c, m)
m = max(b*d, m)
print(m)