import itertools

MAX_DIS = 10**10
N,M,R = map(int,input().split(" "))
r_list = list(map(int,input().split(" ")))
roads = [[MAX_DIS]*N for i in range(N)]
for i in range(N):
    roads[i][i] = 0
for i in range(M):
    A,B,C = map(int,input().split(" "))
    roads[A-1][B-1] = C
    roads[B-1][A-1] = C
for k in range(N):
    for i in range(N):
        for j in range(N):
            roads[i][j] = min(roads[i][j],roads[i][k]+roads[k][j])
min_dis = MAX_DIS
for directions in itertools.permutations(r_list):
    distance  = 0
    for dir in range(1,len(directions)):
        distance += roads[directions[dir-1]-1][directions[dir]-1]
    if distance < min_dis:
        min_dis =distance
print(min_dis)
