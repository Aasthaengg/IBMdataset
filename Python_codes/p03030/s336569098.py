N = int(input())

cities = {}
for i in range(1, N + 1):
    s, p = input().split()
    p = int(p)
    if s in cities:
        cities[s].append((p, i))
    else:
        cities[s] = [(p, i)]
for k in cities.keys():
    cities[k] = list(sorted(cities[k], key=lambda x: x[0], reverse=True))

names = sorted(cities)
for name in names:
    for p, i in cities[name]:
        print(i)
