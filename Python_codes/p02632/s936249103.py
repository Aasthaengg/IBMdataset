MOD = 10**9 + 7
K = int(input())
S = input()


N = len(S)
M = K+N
s = [pow(26,K,MOD)]

r26 = pow(26,MOD-2,MOD)
for i in range(1,K+1):
    t = s[-1]
    t *= r26
    t *= 25
    t *= N+i-1
    t *= pow(i,MOD-2,MOD)
    t %= MOD
    s.append(t)


ans = sum(s) % MOD
print(ans)



