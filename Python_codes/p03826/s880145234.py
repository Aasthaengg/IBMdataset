a, b, c, d = (int(x) for x in input().split())

area1 = a * b
area2 = c * d

area_list = [area1, area2]
area_list.sort()

print(area_list[1])
