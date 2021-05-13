N=int(input())
S=list(input())

M=0
for i in range(1,N):
    M=max(M,len(set(S[:i])&set(S[i:])))
print(M)
