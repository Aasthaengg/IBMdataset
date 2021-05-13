N = int(input())

vac = []
for i in range(N):
    vac.append(list(map(int, input().split())))
    
DP = [[0 for _ in range(3)] for _ in range(N+1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if(j == k):
                continue
            DP[i+1][k] = max(DP[i+1][k], DP[i][j]+vac[i][k])
ans = 0
for i in DP[N]:
    ans = max(ans, i)
print(ans)