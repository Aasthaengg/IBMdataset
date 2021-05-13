N, A, B = map(int, input().split())
Xlist = list(map(int, input().split()))
cost = 0
for i in range(1, N):
    dis = Xlist[i] - Xlist[i - 1]
    cost += min(dis * A, B)
print(cost)
