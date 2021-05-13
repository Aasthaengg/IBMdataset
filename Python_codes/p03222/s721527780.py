H,W,K = map(int,input().split())
move= [0]*(W-1)
count = 0
MOD = 10**9+7

if W == 1:
    print(1)
    exit()

for i in range(2**(W-1),2**W):
    b = bin(i)[3:]
    flag = True
    for j in range(W-2):
        if b[j] == '1' and b[j+1] == '1':
            flag = False
    if flag :
        count += 1
        for j in range(W-1):
            move[j] += int(b[j])

DP = [[0]*W for i in range(H+1)]
DP[0][0] = 1
for i in range(H):
    for j in range(W):
        if j == 0:
            DP[i+1][j] = (DP[i][j]*(count - move[0]) + DP[i][j+1]*move[0])%MOD
        elif j == W-1:
            DP[i+1][j] = (DP[i][j-1] * move[j-1] + DP[i][j]*(count - move[j-1])) % MOD
        else:
            DP[i+1][j] = (DP[i][j-1] * move[j-1] + DP[i][j]*(count - move[j] - move[j-1]) + DP[i][j+1]*move[j]) % MOD
print(DP[-1][K-1])