[N,K] = list(map(int,input().split()))
S = 0
out = [0]*(K+1)
p = 10**9+7
for i in range(K):
    X = K-i
    out[X] = pow(int(K/X),N,p)
    t=2
    while t*X<=K:
        out[X] = out[X]-out[t*X]
        t+=1
    S = (S + X*out[X])%p
print(S)