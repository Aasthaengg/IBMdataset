n,a,b = map(int,input().split())
l = []

l.append(min(a,b))

if n >= a + b:
    l.append(0)
else:
    l.append(a + b - n)

print(l[0],l[1])