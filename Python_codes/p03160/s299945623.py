N = int(input())
l = list(map(int,input().split()))
cost = [0] * N
cost[1] = abs (l[1] - l[0])

for i in range(2,N):
    cost[i] = min(cost[i-1]+abs(l[i]-l[i-1]), cost[i-2]+abs(l[i]-l[i-2]))
print(cost[N-1])        