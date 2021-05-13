x = map(int, raw_input().split(' '))
a = tuple(x[:2])
b = tuple(x[2:])
vector = [-(b[1] - a[1]), (b[0] - a[0]) ]

c = [b[0] + vector[0],b[1] + vector[1] ]
d = [a[0] + vector[0],a[1] + vector[1] ]  

print c[0],c[1], d[0],d[1]