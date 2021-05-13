from bisect import bisect_left
n, m = map(int, input().split())
city_list = [[0] for _ in range(n + 1)]
city = [[]]
for _ in range(m):
    p, y = map(int, input().split())
    city_list[p].append(y)
    city.append([p, y])
for i in range(1, n + 1):
    city_list[i].sort()
for i in range(1, m + 1):
    ID = ''
    p = city[i][0]
    order = str(bisect_left(city_list[p], city[i][1]))
    p = str(p)
    ID = ID + ('0' * (6 - len(p)))
    ID += p
    ID += ('0' * (6 - len(order)))
    ID += order
    print(ID)