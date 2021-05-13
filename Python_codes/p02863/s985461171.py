N,T=[int(s) for s in input().split()]
food=[[int(s) for s in input().split()] for i in range(N)]
food.sort()

#i番目までの料理でt秒以内に食べきるときのDP
DP=[[0 for t in range(T)] for i in range(N)]
for i in range(N):
  time,point=food[i]
  for t in range(min([T,time])):
    DP[i][t]=DP[i-1][t]
  for t in range(time,T):
    DP[i][t]=max([DP[i-1][t] , DP[i-1][t-time]+point])

#i番目の料理を最後に注文することを考える
ls=[DP[i-1][T-1]+food[i][1] for i in range(1,N)]
ls.append(food[0][1])
print(max(ls))  