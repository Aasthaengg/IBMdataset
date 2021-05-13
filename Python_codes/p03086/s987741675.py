S=input()
N=len(S)
ans=0
for l in range(N):
    for r in range(l+1,N+1):
        for c in S[l:r]:
            if c not in "ACGT":
                break
        else:
            ans=max(ans,r-l)
print(ans)
