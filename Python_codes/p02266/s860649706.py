str = list(input())

a = []
all = 0
areas = []
for i in range(len(str)):
    if str[i] == "\\":
        a.append(i)
    elif str[i] == "/" and len(a) > 0:
        j = a.pop()
        b = i - j
        all += b
        while(len(areas) > 0 and areas[-1][0] > j):
            b += areas.pop()[1]
        areas.append([j, b])

print(int(all))
if len(areas) > 0:
    print(len(areas), *[areas[i][1] for i in range(len(areas))])
else:
    print(0)


