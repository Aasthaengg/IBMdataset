N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [0] * N
for i in range(1, N):
    tmp = []
    for j in range(K):
        if (i - j - 1) < 0:
            break
        tmp.append(dp[i-j-1] + abs(H[i]-H[i-j-1]))
    dp[i] = min(tmp)
    # print("tmp", tmp)
    # print("dp ", dp)
print(dp[-1])