x1, y1, x2, y2 = list(map(float, input().split()))
dist = (((x1 - x2)**2 + (y1 - y2)**2)**(1/2))
print("{:.6f}".format(dist))