n = input().strip()

x1,y1,x2,y2 = [ float(i) for i in n.split() ]

dx = abs(x1 - x2)
dy = abs(y1 - y2)

dist = ( dx**2 + dy**2) ** 0.5

print(dist)
