N = int(input())
A = list(map(int,input().split()))
A = [0] + A  #単純にリスト横につなげる
A.append(0)

cost = [0]*(N+1)
for i in range(0,N+1):
    cost[i] = abs(A[i+1] - A[i])
ini = sum(cost)

for i in range(1,N+1):  #iが取りやめた奴
    dam = ini
    dam -= cost[i-1]
    dam -= cost[i]
    dam += abs(A[i+1] - A[i-1])
    print(dam)
