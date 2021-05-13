H, W, K = map(int, input().split())
MOD = 10**9 + 7
if W == 1:
    print(1)
    exit()
MR = [0] * W
ML = [0] * W
MS = [0] * W
for i in range(1 << (W-1)):
    S = bin(i)[2:]
    S = "0"*(W-1-len(S)) + S
    if S.find("11") >= 0:
        continue
    for j, s in enumerate(S):
        if s == "1":
            MR[j] += 1
            ML[j+1] += 1
    for j, (s1, s2) in enumerate(zip("0"+S, S+"0")):
        if s1 == s2 == "0":
            MS[j] += 1

DP = [[0] * W for _ in range(H+1)]
DP[0][0] = 1
for h in range(H):
    for w in range(W-1):
        DP[h+1][w+1] += DP[h][w] * MR[w] % MOD
        DP[h+1][w] += DP[h][w+1] * ML[w+1] % MOD
    for w in range(W):
        DP[h+1][w] += DP[h][w] * MS[w] % MOD

print(DP[H][K-1] % MOD)