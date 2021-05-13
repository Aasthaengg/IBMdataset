#coding:utf-8
n = int(input())
Q = [1]
M = [[False for i in range(n)] for j in range(n)]
dataList = []
for i in range(n):
    data = list(map(int,input().split()))
    dataList.append(data)
    for j in range(data[1]):
        v = data[j+2] - 1
        M[i][v] = True
color = ["white" for i in range(n)]
d = [-1 for i in range(n)]
d[0] = 0
while Q != []:
    u = Q.pop(0) - 1
    color[u] = "gray"
    data = dataList[u]
    for i in range(data[1]):
        v = data[i+2] - 1
        if M[u][v] == True and color[v] == "white":
            color[v] = "gray"
            d[v] = d[u] + 1
            Q.append(v+1)
    color[u] = "black"

for i,j in enumerate(d,1):
    print(i,j)
    
