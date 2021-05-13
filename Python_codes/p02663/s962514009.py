h1,m1,h2,m2,k = map(int,input().split())
d1 = h1 * 60 + m1
d2 = h2 * 60 + m2
print(d2 - d1 - k)