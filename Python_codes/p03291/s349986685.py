S = input()
MOD = 10**9+7
DP = [0]*14 # A,AB,ABC,AB?,A?,A?C,A??,?,?B,?BC,?B?,??,??C,???
for i in range(len(S)):
    if S[i] == "A":
        DP[0] += 1
    elif S[i] == "B":
        for i in range(2,5,2):
            DP[i] += DP[i//2-1] 
            DP[i] %= MOD
    elif S[i] == "C":
        for i in range(6,13,2):
            DP[i] += DP[i//2-1]
            DP[i] %= MOD
    elif S[i] == "?":
        for i in range(6,13,2):
            DP[i+1] += DP[i//2-1]
            DP[i+1] %= MOD
        for i in range(2,5,2):
            DP[i+1] += DP[i//2-1] 
            DP[i+1] %= MOD    
        DP[1] += 1
q = DP[1]
Q0 = 3**q % MOD
Q1 = int(3**(q-1) % MOD)
Q2 = int(3**(q-2) % MOD)
Q3 = int(3**(q-3) % MOD)
Q = [0,0,0,0,0,0,Q0,Q1,Q1,Q2,Q1,Q2,Q2,Q3]
ans = 0
for i in range(14):
    ans += DP[i]*Q[i] % MOD
print(ans%MOD)