n = int(input())
a = list(map(int,input().split()))
cost = [0] + a + [0]

q = [0] * (n + 2)
SUM = 0
for i in range(n + 1):
    temp = abs(cost[i + 1] - cost[i])
    SUM += temp
    q[i] += temp
    q[i + 1] += temp
#print(SUM)

for i in range(n):
    temp = abs(cost[i + 2] - cost[i])
    print(SUM + temp - q[i + 1])