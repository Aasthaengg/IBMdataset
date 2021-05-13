n, m = map(int, input().split())
cities = {}
for i in range(n):
    cities[i+1] = 0
for j in range(m):
    a, b = map(int, input().split())
    cities[a] += 1
    cities[b] += 1
for k in cities.values():
    print(k)