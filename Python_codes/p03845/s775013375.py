n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [list(map(int, input().split())) for i in range(m)]

for i in range(m):
    time = [x for x in t]
    time[p[i][0] - 1] = p[i][1]
    print(sum(time))
