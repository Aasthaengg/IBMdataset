N, Ma, Mb = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
DP = [0]*(N+1)
for i in range(N+1):
    DP[i] = [[float("inf")]*(10*N+1) for i in range(10*N+1)]
for i in range(N+1):
    DP[i][0][0] = 0
for i in range(N):
    for j in range(1, 10*N+1):
        for k in range(1,10*N+1):
            if DP[i+1][j][k] > DP[i][j-A[i][0]][k-A[i][1]]+A[i][2] and j-A[i][0] >= 0 and k-A[i][1] >= 0:
               DP[i+1][j][k] = min(DP[i][j-A[i][0]][k-A[i][1]]+A[i][2], DP[i][j][k])
            else:
                DP[i+1][j][k] = DP[i][j][k]
kouho = set()
for i in range(1, 10*N+1):
    if Ma*i < 10*N+1 and Mb*i < 10*N+1:
        if DP[N][Ma*i][Mb*i] == float("inf"):
            continue
        else:
            kouho.add(DP[N][Ma*i][Mb*i])
    else:
        break
if len(kouho) == 0:
    print(-1)
else:
    print(min(kouho))
                

