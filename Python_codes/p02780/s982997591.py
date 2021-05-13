N,K=map(int,input().split())
P=[0]+list(map(int,input().split()))

S=[0]*(N+1)
for i in range(1,N+1):
    S[i]=S[i-1]+P[i]

M=-1
for j in range(N-K+1):
    M=max(M,S[j+K]-S[j])
print((M+K)/2)
