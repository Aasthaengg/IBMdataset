N,Limit = (int(T) for T in input().split())
Flag = False
CostMax = 1001
for R in range(0,N):
    Cost,Time = (int(T) for T in input().split())
    if Time<=Limit and Cost<CostMax:
        CostMax = Cost
        Flag = True
print(['TLE',CostMax][Flag])