l = [0, 0, 0]
l[0], l[1], l[2] = map(int, input().split())
l.sort()
print(l[2]*10+l[1]+l[0])