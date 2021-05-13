N,K = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i] = format(A[i],'050b')
#print(A)
K = format(K,'050b')
lis = [[0] * 2 for i in range(51)]
for i in range(50):
    for j in range(N):
        lis[i+1][int(A[j][i])] += 1
    lis[i+1].reverse()
# print(K)
#print(lis)

dp = [[-1] * 2 for  i in range(51)]
dp[0][0] = 0
for i in range(50):
    nd = int(K[i])
    for j in range(2):
        if dp[i][j] == -1:
            continue
        for d in range(2):
            ni = i+1
            nj = j
            if j == 0:
                if d > nd:
                    continue
                if d < nd:
                    nj = 1
            dp[ni][nj] = max(dp[ni][nj],dp[i][j] + (lis[ni][d] * 2**(49-i)))

# print(dp)
print(max(dp[50][0],dp[50][1]))
