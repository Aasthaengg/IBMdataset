MOD = 1000000007
H, W, K = map(int, input().split())
table = [[0, 0, 0] for i in range(9)]

for i in range(2 ** (W-1)):
    n = [i & 2**j for j in range(8)]
    
    for i in range(7):
        if n[i] and n[i+1]:
            break
    else:
        i = 0
        while i < W:
            if not n[i]:
                table[i+1][1] += 1
                i += 1
            else:
                table[i+1][2] += 1
                table[i+2][0] += 1
                i += 2
    
dp = [[0 for i in range(W+2)] for j in range(H+1)]
dp[0][1] = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        a = dp[i-1][j-1] * table[j][0]
        b = dp[i-1][j] * table[j][1]
        c = dp[i-1][j+1] * table[j][2]
        dp[i][j] = (a+b+c) % MOD
            
print(dp[H][K])