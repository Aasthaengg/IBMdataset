ab = [list(map(int, input().split())) for _ in range(3)]
road = [0] * 4
for a, b in ab:
    road[a-1] += 1
    road[b-1] += 1
road.sort()
if road[0]==road[1] and road[2]==road[3]: print("YES")
else: print("NO")