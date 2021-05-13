N, M = map(int,input().split())
road = [input().split() for i in range(M)]
for i in range(N):
    num = 0
    for l in range(M):
        num = num + road[l].count(str(i+1))
    print(num)