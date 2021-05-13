N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
city = [0]*N
for r in road:
    city[r[0] - 1] += 1
    city[r[1] - 1] += 1
print(*city,sep="\n")