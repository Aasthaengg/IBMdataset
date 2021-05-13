N = int(input())
DP = [0] * (N+1)
DP[0] = 1
su = [0] * (2*(10**5)+1)
prev = None
MOD = 10**9+7
for i in range(N):
    C = int(input())
    if prev == C:
        DP[i+1] = DP[i]
    else:
        su[C] += DP[i]
        su[C] %= MOD
        DP[i+1] = su[C]
    DP[i+1] %= MOD
    prev = C
print(DP[N])