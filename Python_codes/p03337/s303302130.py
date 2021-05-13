a,b = map(int,input().split())
c = []
c.append(a*b)
c.append(a+b)
c.append(a-b)
c = sorted(c)
print(c[2])