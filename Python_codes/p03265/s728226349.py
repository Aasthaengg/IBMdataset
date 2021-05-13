xy = list(map(int, input().split()))
xy1 = xy[0:2]
xy2 = xy[2:4]

d1 = xy2[0] - xy1[0]
d2 = xy2[1] - xy1[1]

xy3 = [xy2[0] - d2, xy2[1] + d1]
xy4 = [xy3[0] - d1, xy3[1] - d2]

print(*(xy3 + xy4))