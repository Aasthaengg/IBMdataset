# みんなのプロコン 2019: B – Path
a, b = [], []
for _ in range(3):
    tmp = input().split()
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))

paths = a + b
passed_cities = []

for city in range(1, 5):
    passed_cities.append(paths.count(city))

print('NO' if max(passed_cities) == 3 else 'YES')