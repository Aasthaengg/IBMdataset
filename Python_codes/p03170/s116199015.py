n,k = map(int,input().split())
A = list(map(int,input().split()))
dp = [-1]*(k+1) #dp[i]:i個の山の勝敗
dp[0] = -1 #後手の勝ち
for i in range(1,k+1):
    for a in A:
        if a <= i and dp[i-a] == -1:
            dp[i] = 1
            break

#print(dp)

print("First" if dp[k] == 1 else "Second")