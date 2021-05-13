N,M=map(int,input().split())
roads = [0]*N
for _ in range(M):
    a,b=map(int,input().split())
    roads[a - 1] += 1
    roads[b - 1] += 1

for i in roads:
    print(i)
