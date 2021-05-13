#105_D
N,M=map(int,input().split())
A=list(map(int,input().split()))
S=[0]*(N+1)
for i in range(N):
    S[i+1]=S[i]+A[i]
S_Mod=[S[i]%M for i in range(N+1)]
T=sorted(S_Mod)

cnt=0
tmp=1
for i in range(N):
    if T[i]==T[i+1]:
        tmp+=1
    else:
        cnt+=tmp*(tmp-1)//2
        tmp=1
cnt+=tmp*(tmp-1)//2

print(cnt)