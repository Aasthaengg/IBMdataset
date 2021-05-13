mod = 10**9+7
L = input()
l = len(L)
DP = [[0,0] for _ in range(l)] #上から決めていく、0は一致、1は小さいことが確定
DP[0][0] = 2
DP[0][1] = 1
for i in range(1,l):
    if L[i] == '0':
        DP[i][0] = DP[i-1][0]
        DP[i][1] = DP[i-1][1]*3 % mod
    else:
        DP[i][0] = DP[i-1][0]*2 % mod
        DP[i][1] = (DP[i-1][0]+DP[i-1][1]*3) % mod
print((DP[l-1][0]+DP[l-1][1]) % mod)