MOD = (10**9)+7

def wari(x):
    return pow(x,MOD-2,MOD)

N,K = map(int,input().split())
fact = [1]*(N+1)#階乗入れます
for i in range(1,N+1,1):
    fact[i] =  (i*fact[i-1])%MOD

ans = [0]*(K+1)

for i in range(1,K+1,1):
    if i > N - K + 1:
        break
    ans[i] = (fact[K-1]*fact[N-K+1])%MOD
    ans[i] = (ans[i]*wari(fact[K-i]))%MOD
    ans[i] = (ans[i]*wari(fact[i-1]))%MOD
    ans[i] = (ans[i]*wari(fact[N-K-i+1]))%MOD
    ans[i] = (ans[i]*wari(fact[i]))%MOD
    

print(" ".join(list(map(str,ans[1:K+1]))))