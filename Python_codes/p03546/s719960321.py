H,W=map(int,input().split())
numbers=[list(map(int,input().split())) for _ in range(10)]
A=[list(map(int,input().split())) for _ in range(H)]
cost=[[1001 for _ in range(10)] for _ in range(10)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j] , numbers[i][j] , numbers[i][k] + numbers[k][j] ,
                             cost[i][k] + cost[k][j] , numbers[i][k] + cost[k][j],
                             numbers[i][k] + cost[k][j])
ans=0
for a in A:
    for a_ in a:
        if a_ == 1 or a_ == -1:
            pass
        else:
            ans+=cost[a_][1]
print(ans)
