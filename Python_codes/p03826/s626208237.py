
lst = input().split()


for i in range(len(lst)):
   lst[i] = int(lst[i])


area1 = lst[0] * lst[1]
area2 = lst[2] * lst[3]

areas = [area1, area2]
areas.sort()


print(areas[1])
