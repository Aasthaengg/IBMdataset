N,K = map(int,input().split())
p = list(map(int,input().split()))

e = sum(range(1,p[0]+1))/p[0]
S = [e]

for i in range(1,N):
    ex = p[i]*(p[i]+1) / (2*p[i])
    S.append(ex + S[i-1])

ans = S[K-1]
for i in range(K,N):
    ans = max(ans,S[i]-S[i-K])

print(ans)
