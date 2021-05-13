n, m = map(int, input().split())
p, y = zip(*[map(int, input().split()) for _ in range(m)])

city_data = {}
for i in range(m):
    city_data[i] = [p[i], y[i], None]

cities = list(city_data.keys())
cities.sort(key=lambda city: city_data[city])

pref = None
for city in cities:
    if city_data[city][0] == pref:
        yidx += 1
    else:
        yidx = 1
        pref = city_data[city][0]
    city_data[city][2] = '{:06d}{:06d}'.format(pref, yidx)

for i in range(m):
    print(city_data[i][2])
