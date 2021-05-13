N = int(input())
P = list(map(int,input().split()))
mini = 10000000000000
ansL = [0]*N


for i in range(N):
    if P[i] <= mini:
        ansL[i] = 1
        mini = P[i]

print(ansL.count(1))
