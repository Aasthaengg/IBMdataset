from collections import Counter
N=int(input())
S=input()
C=Counter(S)
nr=C["R"]
ng=C["G"]
nb=C["B"]
ans=nr*ng*nb
for i in range(N-2):
    for j in range(i+1,N-1):
        k=j+j-i
        if k<N:
            if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
                ans-=1

print(ans)
