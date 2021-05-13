n = int(input())
votelist = [list(map(int, input().split())) for _ in range(n)]

chlist = votelist[0]
for i in range(1, n):
    x = max(-(chlist[0]*-1 // votelist[i][0]), -(chlist[1]*-1 // votelist[i][1]))
    chlist[0] = votelist[i][0] * x
    chlist[1] = votelist[i][1] * x
    
print(sum(chlist))