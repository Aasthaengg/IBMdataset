import copy

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
dis = copy.deepcopy(a)

def warshall_floyd(dis):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    return dis

data = warshall_floyd(dis)
flag = True
for i in range(n):
    for j in range(i + 1, n):
        if data[i][j] < a[i][j]:
            flag = False
            break
    if flag == False:
        break
if flag == False:
    print(-1)
else:
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                if k == i or k == j:
                    continue
                if data[i][k] + data[k][j] == data[i][j]:
                    break
            else:
                count += data[i][j]
    print(count)