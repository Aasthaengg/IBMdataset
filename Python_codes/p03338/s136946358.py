N=int(input())
S=list(str(input()))
nax=0
for i in range(1,N-1):
    nax=max(nax,len(set(S[:i])&set(S[i:])))

print(nax)