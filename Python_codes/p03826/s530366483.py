e = [int(e) for e in input().split()]
area_1 = e[0] * e[1]
area_2 = e[2] * e[3]
if area_1 >= area_2:
    print(area_1)
else:
    print(area_2)