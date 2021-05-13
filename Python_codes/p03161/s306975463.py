# EDPC B Frog 2
N, K = map(int, input().split())
H = list(map(int,input().split()))

cost = [float("inf")]*N
cost[0] = 0
cost[1] = abs(H[1]-H[0])

for i in range(2,N):
    for k in range(1,min(K,i)+1):
        cost[i] = min(cost[i], cost[i-k]+abs(H[i]-H[i-k]))

print(cost[N-1])
