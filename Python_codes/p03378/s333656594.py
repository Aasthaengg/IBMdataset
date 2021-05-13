N,M,X=map(int,input().split())
A=list(map(int,input().split()))

box = [0]*(N+1)

for i in range(M):
    box[A[i]] = 1

cost_l = 0
for i in range(X+1):
    cost_l += box[i]
cost_r = 0
for i in range(X,N+1):
    cost_r += box[i]

print(min(cost_l,cost_r))