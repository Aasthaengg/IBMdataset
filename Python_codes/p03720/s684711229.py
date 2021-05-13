N,M = [int(i) for i in input().split()]
road = [0]*N
for _ in range(M):
    a,b = [int(i)-1 for i in input().split()]
    road[a] += 1
    road[b] += 1
print("\n".join(map(str, road)))