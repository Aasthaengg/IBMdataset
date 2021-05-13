N = int(input())
K = int(input())
X = int(input())
Y = int(input())
cost = 0
for i in range(N):
    if 1+i <= K:
        cost += X
    if i+1 > K:
        cost += Y
print(cost)