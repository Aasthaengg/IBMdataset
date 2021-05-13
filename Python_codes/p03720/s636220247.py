from collections import defaultdict

n, m = list(map(int, input().split()))
ab_list = [list(map(int, input().split())) for _ in range(m)]

towns_road = defaultdict(list)
for a, b in ab_list:
    towns_road[a].append(b)
    towns_road[b].append(a)

for i in range(1, n + 1):
    print(len(towns_road[i]))
