import sys
input = sys.stdin.readline

h, w, d = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(h)]
q = int(input())
lr = [[int(x) for x in input().split()] for _ in range(q)]

dic = {}

for i in range(h):
    for j in range(w):
        dic[a[i][j]] = (i, j)

dis = {}

for i in range(1, d + 1):
    dis[i] = 0
    while i + d <= h * w:
        dis[i + d] = dis[i] + abs(dic[i + d][0] - dic[i][0]) + abs(dic[i + d][1] - dic[i][1])
        i += d

for i in range(q):
    l, r = lr[i]
    print(dis[r] - dis[l])


