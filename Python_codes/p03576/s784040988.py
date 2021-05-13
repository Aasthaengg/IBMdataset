N,K = map(int,input().split())

P = []

for i in range(N):
    P.append(list(map(int,input().split())))

x = []
y = []
for i in range(N):
    x.append(P[i][0])
    y.append(P[i][1])

x.sort()
y.sort()

num = [[0]*len(y) for i in range(len(x))]
data = [[0]*len(y) for i in range(len(x))]

for i in range(N):
    for j in range(len(x)):
        if P[i][0] == x[j]:
            x0 = j
            break
    for j in range(len(y)):
        if P[i][1] == y[j]:
            y0 = j
            break
    data[x0][y0] += 1

num[0][0] = data[0][0]

for i in range(1,len(x)):
    num[i][0] = num[i-1][0] + data[i][0]

for i in range(1,len(y)):
    num[0][i] = num[0][i-1] + data[0][i]

for i in range(1,len(x)):
    for j in range(1,len(y)):
        num[i][j] = num[i-1][j] + num[i][j-1] - num[i-1][j-1] + data[i][j]

can = []
for i in range(1,len(x)-1):
    for j in range(i+1,len(x)):
        for k in range(1,len(y)-1):
            for l in range(k+1,len(y)):
                if num[j][l] - num[j][k-1] - num[i-1][l] + num[i-1][k-1] >= K:
                    can.append((x[j]-x[i])*(y[l]-y[k]))
for i in range(len(x)):
    for j in range(1,len(y)-1):
        for k in range(j+1,len(y)):
            if num[i][k] - num[i][j-1] >= K:
                can.append((x[i]-x[0])*(y[k]-y[j]))

for i in range(1,len(x)-1):
    for j in range(i+1,len(x)):
        for k in range(len(y)):
            if num[j][k] - num[i-1][k] >= K:
                can.append((x[j]-x[i])*(y[k]-y[0]))

for i in range(len(x)):
    for j in range(len(y)):
        if num[i][j] >= K:
            can.append((x[i]-x[0])*(y[j]-y[0]))


#print("x",x)
#print("y",y)
#print("data",data)
#print("num",num)
#print("can",can)
print(min(can))