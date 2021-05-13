num = [0]
N, X = map(int, input().split())
[num.append(i) for i in list(map(int, input().split()))]

cost = 0
for i in range(1, N+1):
    if num[i-1] + num[i] > X:
        newcost = num[i-1] + num[i] - X
        num[i] -= newcost
        cost += newcost

print(cost)
