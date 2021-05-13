S=input()
N=len(S)+1
L=[0]*N
R=[0]*N
ans=[0]*N
for i in range(1,N):
    if S[i-1]=='<':
        L[i]=L[i-1]+1
    if S[N-i-1]=='>':
        R[N-i-1]=R[N-i]+1
for i in range(N):
    ans[i]=max(L[i], R[i])
print(sum(ans))