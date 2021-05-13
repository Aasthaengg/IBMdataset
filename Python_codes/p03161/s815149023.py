N,K = map(int,input().split())
h = list(map(int,input().split()))

cost = [0]
for i in range(2,N+1):
    cost.append( min([cost[j] + abs(h[i-1]-h[j]) for j in range(max(0,i-K-1), i-1)]) )
print(cost[-1])
