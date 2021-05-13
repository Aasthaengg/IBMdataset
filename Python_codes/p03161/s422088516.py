N,k = map(int,input().split())
l = list(map(int,input().split()))
cost = [0] * N

for i in range(1,N):
    temp = []
    cost[i] = min([cost[j]+abs(l[i]-l[j]) for j in range(max(0,i-k),i)])
print(cost[N-1])