N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]


city = [0]*N
for i in range(M):
    city[ab[i][0]-1] += 1
    city[ab[i][1]-1] += 1

for number in city:
    print(number)
