s = int(input())
MOD = 10**9 + 7
C = [0]*(s + 1)
C[0] = 1
for n in range(3, s+1): # n:[3,s]
    for i in range(3, n+1): # i:[3,n], sum(C[0,n-3])
        C[n] += C[n-i]
        C[n] %= MOD
print(C[s])
