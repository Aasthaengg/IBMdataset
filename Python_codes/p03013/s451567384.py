N,M = (int(x) for x in input().split())
Broken = [True]*(N+1)
for TM in range(0,M):
    Broken[int(input())] = False

DP = [1]+[0]*N
for Now in range(0,N):
    for Next in range(Now+1,min(N+1,Now+3)):
        if Broken[Next]==True: DP[Next] += DP[Now]
print(DP[N]%1000000007)