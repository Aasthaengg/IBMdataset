S=input()
T=input()
N=len(S)
n=len(T)
ans=n
for i in range(N-n+1):
    ans=min(ans,sum(S[i+j]!=T[j] for j in range(n)))
print(ans)
