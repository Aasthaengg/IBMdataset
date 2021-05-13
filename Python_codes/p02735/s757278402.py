H, W = map(int, input().split())
S = [input() for _ in range(H)]

cost = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i == j == 0: 
            continue
        if i == 0:
            cost[i][j] = cost[i][j-1] + 1*(S[i][j] != S[i][j-1])
        elif j == 0:
            cost[i][j] = cost[i-1][j] + 1*(S[i][j] != S[i-1][j])
        else:
            cost[i][j] = min(cost[i][j-1] + 1*(S[i][j] != S[i][j-1]), cost[i-1][j] + 1*(S[i][j] != S[i-1][j]))

if S[0][0] == S[-1][-1] == '.':
    ans = cost[-1][-1]//2
elif S[0][0] != S[-1][-1]:
    ans = cost[-1][-1]//2 + 1
else:
    ans = cost[-1][-1]//2 + 1

print(ans)