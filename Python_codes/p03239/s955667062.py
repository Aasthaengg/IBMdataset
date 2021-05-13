N,T = list(map(int,input().split()))
ct = []
for i in range(N):
    ct.append(list(map(int,input().split())))
minCost = 1001
for i in range(N):
    if ct[i][1] <= T and minCost > ct[i][0]:
        minCost = ct[i][0]
if minCost > 1000:
    print("TLE")
else:
    print(minCost)