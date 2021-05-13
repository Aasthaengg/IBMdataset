#coding: utf-8
inf = 100000000
n = int(input())

List = [0] + [list(map(int,input().split())) for i in range(n)]
d = [inf for i in range(n+1)]
color = ["white" for i in range(n+1)]

s = 1
Q = [s]
d[s] = 0
color[s] = "gray"

while Q != []:
    q = Q.pop(0)
    k = List[q][1]
    for i in List[q][2:2+k]:
        if color[i] == "white":
            Q.append(i)
        d[i] = min(d[q] + 1, d[i])
    color[q] = "gray"


for i, dis in enumerate(d[1:], 1):
    if dis == inf:
        dis = -1
    print(i, dis)

