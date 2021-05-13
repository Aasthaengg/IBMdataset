K=int(input())
S=input()
l=len(S)
if l>K:
    S=S[0:K]
    S=S+'...'
    print(S)
else:
    print(S)