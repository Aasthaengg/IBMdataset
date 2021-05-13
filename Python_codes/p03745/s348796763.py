N = int(input())
A = [int(k) for k in input().split()]

#最小の分割数をdpで考える。
dp = (1, 1)#増減　増加
for i in range(1, N):
    if A[i] > A[i-1]:#大きいときは右側更新
        dp = min(dp)+1, min(dp[0]+1, dp[1])
    elif A[i] == A[i-1]:
        pass
    else:#小さいときは左側
        dp = min(dp[0], dp[1]+1), min(dp)+1
    #print(dp)
print(min(dp))