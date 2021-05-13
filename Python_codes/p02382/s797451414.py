import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

D = [0,0,0,0]
dis = []
for i in range(n):
    D[0] += abs(x[i]-y[i])
    D[1] += (x[i]-y[i])**2
    D[2] += abs((x[i]-y[i]))**3
    dis.append(abs(x[i]-y[i]))

D[1] = math.sqrt(D[1])
D[2] = math.pow(D[2],1/3)
D[3] = max(dis)

for i in range(4):
    print(D[i])