data = map(float, raw_input().split())
x1 = data[0]
y1 = data[1]
x2 = data[2]
y2 = data[3]

distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("{:.8f}".format(distance))