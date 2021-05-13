N = int(input())
ab = [list(map(int, input().split())) for i in range(N)]

minAB = [10**10, 10**10]
for x in ab:
    if minAB[1] > x[1]:
        minAB = x[0], x[1]
print(sum(minAB))
